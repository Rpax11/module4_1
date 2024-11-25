from math import inf

def divide(first, second):
    """Деление с возвратом бесконечности при делении на ноль."""
    if second == 0:
        return inf
    else:
        return first / second