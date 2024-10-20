import ast, operator, json

class Node:
    def __init__(self, type, left=None, right=None, value=None):
        self.type = type
        self.left = left
        self.right = right
        self.value = value

def create_rule(rule_string): 
    try: 
        tree = ast.parse(rule_string, mode='eval') 
        return ast_to_node(tree.body) 
    except Exception as e: 
        raise ValueError(f"Invalid rule syntax: {str(e)}")

def ast_to_node(node):
    if isinstance(node, ast.BoolOp):
        return Node('operator', ast_to_node(node.values[0]), ast_to_node(node.values[1]), 'AND' if isinstance(node.op, ast.And) else 'OR')
    elif isinstance(node, ast.Compare):
        left = node.left.id if isinstance(node.left, ast.Name) else None
        right = node.comparators[0].value if isinstance(node.comparators[0], ast.Constant) else None  # Updated here
        op = node.ops[0]
        if isinstance(op, ast.Gt): return Node('operand', value=(left, '>', right))
        elif isinstance(op, ast.Lt): return Node('operand', value=(left, '<', right))
        elif isinstance(op, ast.Eq): return Node('operand', value=(left, '==', right))
        else: raise ValueError(f"Unsupported comparison: {op}")
    else: raise ValueError(f"Unsupported node type: {node}")

def combine_rules(rules):
    nodes = [create_rule(rule) for rule in rules]
    combined = nodes[0]
    for i in range(1, len(nodes)):
        combined = Node('operator', combined, nodes[i], 'OR')  # Combines with OR
    return combined

def evaluate_rule(node, data):
    if node.type == 'operator':
        left_eval = evaluate_rule(node.left, data)
        right_eval = evaluate_rule(node.right, data)
        if node.value == 'AND': return left_eval and right_eval
        elif node.value == 'OR': return left_eval or right_eval
    elif node.type == 'operand':
        attr, op, val = node.value
        if attr not in data: raise ValueError(f"Attribute '{attr}' not found in data")
        if op == '>': return data[attr] > val
        elif op == '<': return data[attr] < val
        elif op == '==': return data[attr] == val
        else: raise ValueError(f"Unsupported operand '{op}'")
    return False

# Sample usage for rules
rule1 = "((age > 30 and department == 'Sales') or (age < 25 and department == 'Marketing')) and (salary > 50000 or experience > 5)"
rule2 = "((age > 30 and department == 'Marketing')) and (salary > 20000 or experience > 5)"
combined_ast = combine_rules([rule1, rule2])
data = {"age": 35, "department": "Sales", "salary": 60000, "experience": 3}
print(evaluate_rule(combined_ast, data))  # Expected output: True



