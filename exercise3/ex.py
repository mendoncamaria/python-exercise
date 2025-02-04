from collections import Counter

def first_non_repeating_character(string):
  """
  Finds the first non-repeating character in a string.

  Args:
    string: The input string.

  Returns:
    The first non-repeating character in the string, or None if no such character exists.
  """
  char_counts = Counter(string)
  for char in string:
    if char_counts[char] == 1:
      return char
  return None

# Example usage
# string = "leetcode"
# result = first_non_repeating_character(string)
# print(f"First non-repeating character: {result}")
