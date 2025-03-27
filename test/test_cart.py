from calculate_cart_total.calculate_cart_total import calculate_total 

# Arrange
# Act
# Assert

# test 1
def test_return_total_price():
    # Arrange
    prices = {
    "apple": 0.75,
    "beans": 2.00,
    "cheese": 2.50,
    "chicken": 4.00,
    "flour": 1.75,
    "onion": 0.50,
    "orange": 0.85,
    "lettuce": 1.25,
    "milk": 3.00,
    "tomato": 0.45
}
    cart = ["milk", "chicken", "beans"]

    # Act
    total = calculate_total(cart)

    # Assert
    assert total == 9
    
# test 2
def test_return_float_if_cart_empty():
    # Arrange
    cart = []
    # Act
    expected = calculate_total(cart)
    
    # Assert
    assert expected == 0.0

def test_drop_the_discount_price_if_there_is_discount():
    prices = {
    "apple": 0.75,
    "beans": 2.00,
    "cheese": 2.50,
    "chicken": 4.00,
    "flour": 1.75,
    "onion": 0.50,
    "orange": 0.85,
    "lettuce": 1.25,
    "milk": 3.00,
    "tomato": 0.45
}
    cart = ["apple", "cheese"]
    discount= 1.0
    expected = calculate_total(cart)
    expected_after_discount = expected - discount
    assert expected == 3.25
    assert expected_after_discount == 2.25
    

    
def test_if_the_list_is_lover_case_or_mixed():
    prices = {
    "apple": 0.75,
    "beans": 2.00,
    "cheese": 2.50,
    "chicken": 4.00,
    "flour": 1.75,
    "onion": 0.50,
    "orange": 0.85,
    "lettuce": 1.25,
    "milk": 3.00,
    "tomato": 0.45
}
    cart = ["Apple", "onIon", "tOmatO"]
    expected = calculate_total(cart)
    
    assert expected == 1.7

def test_if_the_item_dont_excist():
    prices = {
    "apple": 0.75,
    "beans": 2.00,
    "cheese": 2.50,
    "chicken": 4.00,
    "flour": 1.75,
    "onion": 0.50,
    "orange": 0.85,
    "lettuce": 1.25,
    "milk": 3.00,
    "tomato": 0.45
}
cart = ["cherry", "lettuce", "beans"]

expected = calculate_total(cart)

assert expected == 3.25