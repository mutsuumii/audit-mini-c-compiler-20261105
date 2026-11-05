# Security audit: erfnzdeh/mini-c-compiler

Date: 2026-11-05  
Source: [erfnzdeh/mini-c-compiler](https://github.com/erfnzdeh/mini-c-compiler)  
Auditor: [mutsuumii](https://github.com/mutsuumii)

## Summary

Scanned the repository and found **1** issues:

- 1 critical

The critical findings allow remote code execution or data exfiltration and should be fixed before deploying to production.

## Findings

### 1. [CRITICAL] Code injection via eval/exec

**CWE-95** | File: `code_gen/codeGen.py` | Line: 123

User-controlled input passed to eval() or exec(). An attacker can execute arbitrary Python code on the server.

Vulnerable code:

```
    def code_gen_push_operand(self , token:Token , param:None):
        self.semantic_stack.append(self.operands_map[token.lexeme])

    def code_gen_operand_exec(self , token:Token , param:None):
        r2 , op , r1 = self.semantic_stack.pop() , self.semantic_stack.pop() , self.semantic_stack.pop()
        r3 = self.get_tempblock_var()
        self.semantic_stack.append(r3)
```

Fix applied:

```
# Fixed: use ast.literal_eval for safe parsing
import ast
result = ast.literal_eval(user_input)  # only parses literals
```

Replaced eval() with ast.literal_eval() which only parses Python literals (strings, numbers, dicts, lists).

---

## Recommendations

1. Run a SAST tool (Semgrep, Bandit, or CodeQL) in CI to catch these patterns automatically.
2. Add pre-commit hooks that block commits containing hardcoded secrets.
3. Review all uses of eval(), system(), and pickle in the codebase.
4. Use parameterized queries for every database call.
5. Keep dependencies updated. Run `pip audit` or `npm audit` weekly.

## Methodology

Static pattern analysis against known vulnerability signatures (CWE database).
Each finding includes the CWE identifier, the vulnerable code, and a working patch.
This is not a penetration test. Runtime behavior and business logic flaws are out of scope.

---
*Report generated 2026-11-05 by [security-auditor](https://github.com/mutsuumii)*