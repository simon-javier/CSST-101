# predicate_logic.py

def forall(predicate, domain):
    """
    Universal quantifier (FOR ALL).
    Checks if a predicate is true for all elements in the domain.
    
    Args:
        predicate (function): A function that returns a boolean value for each element.
        domain (iterable): The domain over which to apply the predicate.
        
    Returns:
        bool: True if the predicate is true for all elements in the domain.
    """
    return all(predicate(x) for x in domain)

def exists(predicate, domain):
    """
    Existential quantifier (EXISTS).
    Checks if a predicate is true for at least one element in the domain.
    
    Args:
        predicate (function): A function that returns a boolean value for each element.
        domain (iterable): The domain over which to apply the predicate.
        
    Returns:
        bool: True if the predicate is true for at least one element in the domain.
    """
    return any(predicate(x) for x in domain)

