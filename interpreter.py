# interpreter.py

class Interpreter:
    def __init__(self):
        # This dictionary is our 'Memory' or 'Symbol Table'
        self.variables = {}

    def visit(self, node):
        method_name = f'visit_{type(node).__name__}'
        method = getattr(self, method_name)
        return method(node)

    # ... keep your visit_NumberNode and visit_BinOpNode ...

    def visit_VarAssignNode(self, node):
        var_name = node.var_name_token[1]
        value = self.visit(node.value_node)
        self.variables[var_name] = value
        return value

    def visit_VarAccessNode(self, node):
        var_name = node.var_name_token[1]
        val = self.variables.get(var_name)
        if val is None:
            raise NameError(f"Variable '{var_name}' is not defined")
        return val
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

    # interpreter.py

    def visit_IfNode(self, node):
        # 1. Evaluate the condition node
        condition_result = self.visit(node.condition_node)
        
        # 2. Logic: If result is non-zero/True, visit body
        if condition_result:
            return self.visit(node.body_node)
        # 3. Otherwise, visit else_node if it exists
        elif node.else_node:
            return self.visit(node.else_node)
        
        return None