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