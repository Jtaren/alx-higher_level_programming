#!/usr/bin/pyton3

class MyList(list):
  """
  MyList class inherits from list and adds a print_sorted method.

  Attributes:
      (inherited from list)

  Methods:
      print_sorted(): Prints the list elements sorted in ascending order.
  """

  def print_sorted(self):
    """
    Prints the list elements sorted in ascending order.
    """
    print(f"Sorted list: {sorted(self)}")
