# nodes.py

class Node:
    def __repr__(self):
        return f"({self.__class__.__name__})"

class NumberNode(Node):
    def __init__(self, value):
        self.value = value
    def __repr__(self):
        return f"{self.value}"

class BinOpNode(Node):
    def __init__(self, left, op_token, right):
        self.left = left
        self.op_token = op_token
        self.right = right
    def __repr__(self):
        return f"({self.left} {self.op_token[1]} {self.right})"

class VarAssignNode(Node):
    def __init__(self, var_name, value_node):
        self.var_name = var_name
        self.value_node = value_node

# nodes.py (Add these to your existing classes)

class VarAssignNode(Node):
    """Represents 'x = 10'"""
    def __init__(self, var_name_token, value_node):
        self.var_name_token = var_name_token
        self.value_node = value_node
    def __repr__(self):
        return f"({self.var_name_token[1]} = {self.value_node})"

class VarAccessNode(Node):
    """Represents using 'x' in an expression like 'x + 5'"""
    def __init__(self, var_name_token):
        self.var_name_token = var_name_token
    def __repr__(self):
        return f"{self.var_name_token[1]}"
    

class IfNode(Node):
    """Represents 'if condition: body'"""
    def __init__(self, condition_node, body_node, else_node=None):
        self.condition_node = condition_node
        self.body_node = body_node
        self.else_node = else_node
        
    def __repr__(self):
        return f"(IF {self.condition_node} THEN {self.body_node} ELSE {self.else_node})"