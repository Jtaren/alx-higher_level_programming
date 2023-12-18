#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
  """
  Prints up to x elements of a list on the same line, followed by a newline.

  Args:
    my_list: The list to print elements from.
    x: The number of elements to print (can be larger than the list length).

  Returns:
    The number of elements actually printed.
  """
  ret = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            ret += 1
        except IndexError:
            break
    print("")
    return (ret)
