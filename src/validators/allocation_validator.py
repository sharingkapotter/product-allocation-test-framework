def validate_allocation(demand: int, capacity: int, allocated: int):
    """
    Validates allocation business rules.
    """

    assert allocated >= 0, "Allocation cannot be negative"
    assert allocated <= demand, "Allocation exceeds demand"
    assert allocated <= capacity, "Allocation exceeds capacity"
