# logic_operations.py

def and_operation(p, q):
    """
    Logical AND operation.
    Returns True if both p and q are True, otherwise False.
    """
    return p and q

def or_operation(p, q):
    """
    Logical OR operation.
    Returns True if either p or q is True, otherwise False.
    """
    return p or q

def not_operation(p):
    """
    Logical NOT operation.
    Returns the negation of p.
    """
    return not p

def implies_operation(p, q):
    """
    Logical IMPLIES operation.
    Returns True if p implies q (¬p ∨ q).
    """
    return not p or q

def evaluate(statement, values):
    """
    Evaluate a logical statement given a dictionary of truth values.
    
    Args:
        statement (lambda function): Logical expression to evaluate.
        values (dict): Dictionary mapping variables to their truth values.
        
    Returns:
        bool: The truth value of the logical statement.
    """
    return statement(values)

