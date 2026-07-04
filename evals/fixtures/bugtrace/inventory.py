def total_value(items):
    """Sum of price * qty across items.

    items: list of models.Item
    """
    return sum(item.price * item.qty for item in items)
