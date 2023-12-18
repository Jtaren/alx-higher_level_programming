def safe_print_integer(value):
  """
  Prints an integer using "{:d}".format() and returns True if successful.

  Args:
    value: Any value to be checked and printed.

  Returns:
    True if the value is an integer and printed successfully, False otherwise.
  """

  try:
    print("{:d}".format(value))
    return (True)
  except (TypeError, ValueError):
    return (False)
