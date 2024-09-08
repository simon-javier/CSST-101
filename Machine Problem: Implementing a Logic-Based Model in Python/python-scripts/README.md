## Python Scripts

### 1. Propositional Logic Operations

```python
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
```

### 2. Evaluation Function

```python
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
```

### 3. Predicate Logic

```python
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
```

### 4. AI Agent

```python
# ai_agent.py

from logic_operations import and_operation, not_operation

def decide_action(conditions):
    """
    Simple AI agent decision-making based on weather conditions.
    
    Args:
        conditions (dict): Dictionary with keys 'is_raining' and 'has_umbrella'.
        
    Returns:
        str: Decision based on the conditions.
    """
    is_raining = conditions.get('is_raining', False)
    has_umbrella = conditions.get('has_umbrella', False)
    
    if and_operation(is_raining, has_umbrella):
        return "Go outside with umbrella."
    elif not_operation(is_raining):
        return "Go outside."
    else:
        return "Stay indoors."
```
