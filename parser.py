# parser.py
from nodes import NumberNode, BinOpNode, VarAccessNode, IfNode

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
    
    # parser.py (Updated logic)

    def factor(self):
        token = self.current_token
        if token[0] == 'NUMBER':
            self.pos += 1
            return NumberNode(token[1])
        
        # New: Handle Variable Access
        if token[0] == 'IDENT':
            self.pos += 1
            return VarAccessNode(token)
        # ...
        
    def statement(self):
        # New: Check for 'x = ...'
        if self.current_token[0] == 'IDENT':
            var_name = self.current_token
            self.pos += 1
            if self.current_token and self.current_token[0] == 'ASSIGN':
                self.pos += 1
                return VarAssignNode(var_name, self.expression())
            else:
                # If no '=', it's just a variable access in an expression
                self.pos -= 1 
        return self.expression()
    
    # parser.py

    def if_expression(self):
        self.pos += 1 # Skip 'if'
        condition = self.expression() # Get the condition logic
        
        # In a real language, you'd handle braces or indentation here.
        # For 'Cool', let's assume the next 'statement' is the body.
        body = self.statement()
        
        else_node = None
        if self.current_token and self.current_token[0] == 'ELSE':
            self.pos += 1
            else_node = self.statement()
            
        return IfNode(condition, body, else_node)

    def statement(self):
        if self.current_token and self.current_token[0] == 'IF':
            return self.if_expression()
        # ... rest of your statement logic ...