def safe_print_list(my_list=[], x=0):
  """
  Prints up to x elements of a list on the same line, followed by a newline.

  Args:
    my_list: The list to print elements from.
    x: The number of elements to print (can be larger than the list length).

  Returns:
    The number of elements actually printed.
  """

  printed_count = 0
  for i, element in enumerate(my_list):
    try:
      print(element, end="")
      printed_count += 1
      if printed_count == x:
        break
    except TypeError:
      # Ignore elements that can't be printed
      pass

  print()  # Print a newline at the end
  return printed_count
