def fun1(x, y):
    """
    Adds two numbers together.
    Args:
        x (int/float): First number.
        y (int/float): Second number.
    Returns:
        int/float: Sum of x and y.
        Raises:
        ValueError: If x or y is not a number.
    """
    if not (isinstance(x, (int, float)) and isinstance(y, (int, float))):
        raise ValueError("Both inputs must be numbers.")
    
    return x + y

def fun2(x, y):
    """
    Subtracts two numbers.
    Args:
        x (int/float): First number.
        y (int/float): Second number.
    Returns:
        int/float: Difference of x and y.
        Raises:
        ValueError: If x or y is not a number.
    """
    if not (isinstance(x, (int, float)) and isinstance(y, (int, float))):
        raise ValueError("Both inputs must be numbers.")
    return x - y

def fun3(x, y):
    """
    Multiplies two numbers together.
    Args:
        x (int/float): First number.
        y (int/float): Second number.
    Returns:
        int/float: Product of x and y.
        Raises:
        ValueError: If either x or y is not a number.
    """
    if not (isinstance(x, (int, float)) and isinstance(y, (int, float))):
        raise ValueError("Both inputs must be numbers.")
    return x * y

def fun4(x,y,z):
    """
    Adds three numbers together.
    Args:
        x (int/float): First number.
        y (int/float): Second number.
        z (int/float): Third number.
    Returns:
        int/float: Sum of x, y and z.
    """
    total_sum = x + y + z
    return total_sum

def fun5(x, y):
    """
    Divides x by y.

    Args:
        x (int/float): Numerator.
        y (int/float): Denominator.

    Returns:
        int/float: Result of x divided by y.

    Raises:
        ValueError: If x or y is not a number.
        ZeroDivisionError: If y is zero.
    """
    if not (isinstance(x, (int, float)) and isinstance(y, (int, float))):
        raise ValueError("Both inputs must be numbers.")

    if y == 0:
        raise ZeroDivisionError("Cannot divide by zero.")

    return x / y


def fun6(x, y):
    """
    Calculates x raised to the power of y.

    Args:
        x (int/float): Base.
        y (int/float): Exponent.

    Returns:
        int/float: x raised to the power of y.

    Raises:
        ValueError: If x or y is not a number.
    """
    if not (isinstance(x, (int, float)) and isinstance(y, (int, float))):
        raise ValueError("Both inputs must be numbers.")

    return x ** y


def fun7(x, y):
    """
    Calculates the modulus of x and y.

    Args:
        x (int/float): First number.
        y (int/float): Second number.

    Returns:
        int/float: Remainder after dividing x by y.

    Raises:
        ValueError: If x or y is not a number.
        ZeroDivisionError: If y is zero.
    """
    if not (isinstance(x, (int, float)) and isinstance(y, (int, float))):
        raise ValueError("Both inputs must be numbers.")

    if y == 0:
        raise ZeroDivisionError("Cannot calculate modulus with zero.")

    return x % y


def fun8(x, y, z):
    """
    Calculates the average of three numbers.

    Args:
        x (int/float): First number.
        y (int/float): Second number.
        z (int/float): Third number.

    Returns:
        float: Average of x, y and z.

    Raises:
        ValueError: If any input is not a number.
    """
    if not all(isinstance(value, (int, float)) for value in (x, y, z)):
        raise ValueError("All inputs must be numbers.")

    return (x + y + z) / 3


def fun9(x, y, z):
    """
    Returns the largest of three numbers.

    Args:
        x (int/float): First number.
        y (int/float): Second number.
        z (int/float): Third number.

    Returns:
        int/float: Largest number.

    Raises:
        ValueError: If any input is not a number.
    """
    if not all(isinstance(value, (int, float)) for value in (x, y, z)):
        raise ValueError("All inputs must be numbers.")

    return max(x, y, z)


def fun10(x, y, z):
    """
    Returns the smallest of three numbers.

    Args:
        x (int/float): First number.
        y (int/float): Second number.
        z (int/float): Third number.

    Returns:
        int/float: Smallest number.

    Raises:
        ValueError: If any input is not a number.
    """
    if not all(isinstance(value, (int, float)) for value in (x, y, z)):
        raise ValueError("All inputs must be numbers.")

    return min(x, y, z)
