# day2/operations_tool/evaluator.py
import ast
import operator

# mapping AST operator nodes to actual functions
_BIN_OPS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.Pow: operator.pow,
    ast.Mod: operator.mod,
}

_UNARY_OPS = {
    ast.UAdd: lambda x: x,
    ast.USub: lambda x: -x,
}


def _eval_node(node: ast.AST):
    """Évalue récursivement un noeud AST déjà validé comme sûr."""
    if isinstance(node, ast.Expression):
        return _eval_node(node.body)
    if isinstance(node, ast.Constant):  # Python 3.8+
        return node.value
    if hasattr(ast, "Num") and isinstance(node, ast.Num):  # older
        return node.n
    if isinstance(node, ast.BinOp):
        left = _eval_node(node.left)
        right = _eval_node(node.right)
        op_type = type(node.op)
        if op_type not in _BIN_OPS:
            raise ValueError(f"Unsupported binary operator: {op_type}")
        func = _BIN_OPS[op_type]
        return func(left, right)
    if isinstance(node, ast.UnaryOp):
        operand = _eval_node(node.operand)
        op_type = type(node.op)
        if op_type not in _UNARY_OPS:
            raise ValueError(f"Unsupported unary operator: {op_type}")
        func = _UNARY_OPS[op_type]
        return func(operand)

    raise ValueError(f"Unsupported AST node: {type(node)}")


def evaluate(tree: ast.AST):
    """Evaluates a safe AST tree and returns the numeric result."""
    return _eval_node(tree)
