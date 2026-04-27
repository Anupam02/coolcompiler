# main.py
from lexer import lex
from parser import Parser
from interpreter import Interpreter

code = "5 + 2 * 10"
tokens = lex(code)
parser = Parser(tokens)
ast = parser.parse()
interpreter = Interpreter()

result = interpreter.visit(ast)

print(f"Code: {code}")
print(f"AST: {ast}")
print(f"Result: {result}")


# Now we can handle multiple lines!
code_lines = [
    "x = 10",
    "y = 20",
    "x + y * 2"
]

interp = Interpreter()

for line in code_lines:
    tokens = lex(line)
    parser = Parser(tokens)
    ast = parser.statement()
    result = interp.visit(ast)
    print(f"Executed: {line} -> Result: {result}")

print(f"Final Memory State: {interp.variables}")