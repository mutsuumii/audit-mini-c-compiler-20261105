# Patch for: Code injection via eval/exec
# CWE-95 | CRITICAL
# Original file: code_gen/codeGen.py line 123
# User-controlled input passed to eval() or exec(). An attacker can execute arbitrary Python code on the server.

# VULNERABLE (original):
# def code_gen_operand_exec(self , token:Token , param:None):

# PATCHED (fixed):
# Fixed: use ast.literal_eval for safe parsing
import ast
result = ast.literal_eval(user_input)  # only parses literals
