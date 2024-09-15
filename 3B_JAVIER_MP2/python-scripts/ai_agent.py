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

