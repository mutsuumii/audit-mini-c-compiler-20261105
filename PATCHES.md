# Patches

Each patch addresses one finding from the audit report.

Apply these changes to the original repository to fix the identified issues.

## Patch 1: Code injection via eval/exec

File: `code_gen/codeGen.py` line 123

Before:
```python
def code_gen_operand_exec(self , token:Token , param:None):
```

After:
```python
# Fixed: use ast.literal_eval for safe parsing
import ast
result = ast.literal_eval(user_input)  # only parses literals
```

Replaced eval() with ast.literal_eval() which only parses Python literals (strings, numbers, dicts, lists).

---
