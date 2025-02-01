def find_first_repeating_digit(digit_pattern):
    """
    Finds the first repeating digit in a string of digits.

    Args:
        digit_pattern: The string of digits.

    Returns:
        The first repeating digit, or -1 if no digit is repeating.
    """

    seen_digits = set()
    for digit in digit_pattern:
        if digit in seen_digits:
            return int(digit)
        seen_digits.add(digit)
    return -1

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        digit_pattern = input()
        result = find_first_repeating_digit(digit_pattern)
        print(result)
