from calculate_cart_total.calculate_cart_total import calculate_total 

# Test 1
def test_returns_total_price():
    # Arrange
    cart = ["milk", "chicken", "beans"]
    # Act
    total = calculate_total(cart)
    # Assert
    assert total == 9

# Test 2
def test_returns_zero_float_if_cart_empty():
    # Arrange
    cart = []
    # Act
    total = calculate_total(cart)
    # Assert
    assert total == 0.0

# Test 3
def test_ignores_case_of_items():
    # Arrange
    cart = ["Apple", "onIon", "tOmatO"]
    # Act
    total = calculate_total(cart)
    # Assert
    assert total == 1.7

# Test 4
def test_ignores_unknown_items():
    # Arrange
    cart = ["cherry", "lettuce", "beans"]
    # Act
    total = calculate_total(cart)
    # Assert
    assert total == 3.25
    
    # Test 5
# def test_applies_discount_correctly():
#     # Arrange
#     cart = ["apple", "cheese"]
#     discount = 1.0
#     # Act
#     total = calculate_total(cart)
#     total_after_discount = total - discount
#     # Assert
#     assert total == 3.25
#     assert total_after_discount == 2.25