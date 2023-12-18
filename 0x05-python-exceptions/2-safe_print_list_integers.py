#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
  """
  Prints the first x integers from a list on the same line, skipping non-integers.

  Args:
    my_list: The list to print integers from.
    x: The number of elements to access (can be larger than the list length).

  Returns:
    The number of integers actually printed.

  Raises:
    IndexError: If x is larger than the list length.
  """

  printed_count = 0
  for i in range(0, x):
    try:
        print("{:d}".format(my_list[i]), end="")
        printed_count += 1
    except (ValueError,TypeError):
        continue

  print("")
  return (printed_count)
