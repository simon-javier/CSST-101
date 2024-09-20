## Notebook Link
https://colab.research.google.com/drive/18Fb2ktHbjNRG5ucRCzgL1-_uiEXCuKLs?usp=sharing

### 1. Propositional Logic Operations

```python
# AND operation
def and_operation(p, q):
    return p and q

# OR operation
def or_operation(p, q):
    return p or q

# NOT operation
def not_operation(p):
    return not p

# IMPLIES operation
def implies_operation(p, q):
    return not p or q  # p → q is equivalent to ¬p ∨ q
```

### 2. Evaluate Logical Statements

```python
# Evaluation function for logical expressions
def evaluate(statement, values):
    # statement is expected to be a lambda function
    # values is a dictionary { 'p': True, 'q': False, ... }
    return statement(values)
    
# Example usage
values = {'p': True, 'q': False}
statement = lambda vals: implies_operation(vals['p'], vals['q'])
print(evaluate(statement, values))  # Output: False
```

### 3. Extend to Predicate Logic

```python
# FOR ALL (universal quantifier)
def forall(predicate, domain):
    return all(predicate(x) for x in domain)

# EXISTS (existential quantifier)
def exists(predicate, domain):
    return any(predicate(x) for x in domain)

# Example usage
domain = [1, 2, 3, 4]
predicate = lambda x: x % 2 == 0  # Checks if x is even

print(forall(predicate, domain))  # Output: False (not all are even)
print(exists(predicate, domain))  # Output: True (at least one is even)
```

### 4. AI Agent Development

```python
# AI Agent decision logic
def decide_action(conditions):
    is_raining = conditions.get('is_raining', False)
    has_umbrella = conditions.get('has_umbrella', False)
    
    # If it's raining and you have an umbrella, you can go outside
    if and_operation(is_raining, has_umbrella):
        return "Go outside with umbrella."
    # If it's not raining, you can go outside
    elif not_operation(is_raining):
        return "Go outside."
    # Otherwise, stay indoors
    else:
        return "Stay indoors."

# Example scenario
conditions = {'is_raining': True, 'has_umbrella': True}
print(decide_action(conditions))  # Output: Go outside with umbrella.
```
