from app.operations import add, subtract


def test_add_positive():
    # Arrange: expectation is independently calculated.
    a, b = 2, 3
    expected = 5
    # Act
    result = add(a, b)
    # Assert
    assert result == expected


def test_add_negative():
    # Arrange: expectation is independently calculated.
    a, b = -2, -3
    expected = -5
    # Act
    result = add(a, b)
    # Assert
    assert result == expected


def test_add_zero():
    # Arrange: expectation is independently calculated.
    a, b = 0, 6
    expected = 6
    # Act
    result = add(a, b)
    # Assert
    assert result == expected


def test_subtract_positive():
    # Arrange: expectation is independently calculated.
    a, b = 7, 2
    expected = 5
    # Act
    result = subtract(a, b)
    # Assert
    assert result == expected


def test_subtract_negative():
    # Arrange: expectation is independently calculated.
    a, b = -7, -2
    expected = -5
    # Act
    result = subtract(a, b)
    # Assert
    assert result == expected


def test_subtract_negative_result():
    # Arrange: expectation is independently calculated.
    a, b = 2, 5
    expected = -3
    # Act
    result = subtract(a, b)
    # Assert
    assert result == expected
