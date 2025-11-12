# day2/operations_tool/parser.py
import ast

# Liste des nœuds AST autorisés
_ALLOWED_NODES = {
    ast.Expression,
    ast.BinOp,
    ast.UnaryOp,
    ast.Num,  # Python <3.8: Num
    ast.Constant,  # Python >=3.8: Constant (pour nombres)
    ast.Add,
    ast.Sub,
    ast.Mult,
    ast.Div,
    ast.Pow,
    ast.Mod,
    ast.UAdd,
    ast.USub,
    ast.Load,
    ast.Expr,
    ast.Call,  # we'll explicitly reject Call in validation
    ast.Tuple,
    ast.List,
    ast.Subscript,
    ast.Index,
    ast.Slice,
    ast.Attribute,
    ast.Name,
}

# But we'll only accept a safe subset in checking (no Call, no Attribute, no Name)
_SAFE_NODE_TYPES = (
    ast.Expression,
    ast.BinOp,
    ast.UnaryOp,
    ast.Constant,
    ast.Num,
    ast.Add,
    ast.Sub,
    ast.Mult,
    ast.Div,
    ast.Pow,
    ast.Mod,
    ast.UAdd,
    ast.USub,
)


def _is_safe_node(node: ast.AST) -> bool:
    """Vérifie que le noeud et ses enfants sont autorisés."""
    if isinstance(node, _SAFE_NODE_TYPES):
        # check children recursively
        for child in ast.iter_child_nodes(node):
            if not _is_safe_node(child):
                return False
        return True
    else:
        return False


def parse_and_validate(expr: str) -> ast.AST:
    """Parse l'expression en AST, puis vérifie qu'elle contient seulement des noeuds sûrs.
    Lève ValueError si l'expression n'est pas valide ou comporte des éléments non autorisés.
    """
    try:
        tree = ast.parse(expr, mode="eval")
    except SyntaxError as e:
        raise ValueError(f"Syntax error: {e}") from e

    if not _is_safe_node(tree):
        raise ValueError("Expression contains unsafe or unsupported constructs.")
    return tree
