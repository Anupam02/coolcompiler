# interpreter.py

class Interpreter:
    def visit(self, node):
        method_name = f'visit_{type(node).__name__}'
        method = getattr(self, method_name)
        return method(node)

    def visit_NumberNode(self, node):
        return node.value

    def visit_BinOpNode(self, node):
        left = self.visit(node.left)
        right = self.visit(node.right)
        
        op = node.op_token[0]
        if op == 'PLUS': return left + right
        if op == 'MINUS': return left - right
        if op == 'MUL': return left * right
        if op == 'DIV': return left / right