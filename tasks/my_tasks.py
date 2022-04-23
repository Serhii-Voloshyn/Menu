
def reverse_number(number: int) -> int:
    """Returns reversed number

    Keyword arguments:
    number -- integer, given number"""
    assert isinstance(number, int), "Number should be integer"
    assert number > 0, "Number should be greater than 0"

    return int(str(number)[::-1])


def is_3_in_square_of_number(number: int) -> bool:
    """Returns True if 3 is in square of number

    Keyword arguments:
    number -- integer, given number
    """
    assert isinstance(number, int), "Number should be integer"
    assert number > 0, "Number should be greater than 0"

    return '3' in str(number*number)


def get_number_with_largest_sum_of_divisors(a: int, b: int) -> int:
    """Returns number with the largest sum of divisors within range (a, b)

    Keyword arguments:
    a -- integers, start point of the loop
    b -- integers, end point of the loop
    """
    assert isinstance(a, int) and isinstance(b, int), "Boundaries (a and b) should be integers"
    assert b >= a, "Second (b) argument should be bigger than first (a)"

    # List of all sums of divisors
    list_of_sums = [sum(get_divisors_list(number)) for number in range(a, b)]
    # Get the largest sum in list
    max_sum = max(list_of_sums)

    # Get number with the largest sum of divisors
    # Works, while a = 1, b => a
    number_with_max_sum = list_of_sums.index(max_sum) + 1

    return number_with_max_sum


def get_divisors_list(number: int) -> list:
    """Returns list of number divisors

    Keyword arguments:
    number -- integer, given number
    """
    assert isinstance(number, int), "Number should be integer"
    assert number > 0, "Number should be greater than 0"

    return [i for i in range(1, int(number/2) + 1) if number % i == 0] + [number]


def task_322() -> int:
    """Implementation of the task #322.

    Returns number with largest sum of divisors from 1 to 10000
    """
    print("Task 322. Function returns number from 1 to 10000 with largest sum of divisors.")
    # Set boundaries
    a = 1
    b = 10000

    return get_number_with_largest_sum_of_divisors(a, b)


def task_88a() -> bool:
    """Implementation of the task #88a.

    Returns true if square of number contains 3
    """
    print("Task 88 a). Function return true if square of number contains 3")
    print("Number should be integer and greater than 0.")
    try:
        # User input
        number = int(input("Enter n: "))

        # Check if 3 is in number squared
        return is_3_in_square_of_number(number)

    # If user's input is invalid
    except ValueError:
        print("Wrong input!")


def task_88b() -> int:
    """Implementation of the task #88b.
    
    Returns reversed number"""
    print("Task 88b. Function returns reversed number.")
    print("Number should be integer and greater than 0.")
    try:
        # User's input
        n = int(input("Enter n: "))

        # Prints result
        return reverse_number(n)

    # If user's input is invalid
    except ValueError:
        print("Wrong input!")