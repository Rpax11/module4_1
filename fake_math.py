def divide(first, second):
    """Деление с обработкой ошибки деления на ноль."""
    if second == 0:
        return 'Ошибка'
    else:
        return first / second