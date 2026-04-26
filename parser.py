# parser.py
from nodes import NumberNode, BinOpNode

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    @property
    def current_token(self):
        return self.tokens[self.pos] if self.pos < len(self.tokens) else None

    def parse(self):
        return self.expression()

    def factor(self):
        # Handles numbers and parentheses
        token = self.current_token
        if token[0] == 'NUMBER':
            self.pos += 1
            return NumberNode(token[1])
        # Add more logic here for parentheses later!

    def term(self):
        # Handles Multiplication and Division
        node = self.factor()
        while self.current_token and self.current_token[0] in ('MUL', 'DIV'):
            op = self.current_token
            self.pos += 1
            node = BinOpNode(node, op, self.term())
        return node

    def expression(self):
        # Handles Addition and Subtraction
        node = self.term()
        while self.current_token and self.current_token[0] in ('PLUS', 'MINUS'):
            op = self.current_token
            self.pos += 1
            node = BinOpNode(node, op, self.term())
        return node