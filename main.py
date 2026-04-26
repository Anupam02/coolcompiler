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