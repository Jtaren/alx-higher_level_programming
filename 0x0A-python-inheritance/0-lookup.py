def lookup(obj):
  """
  Returns a list of available attributes and methods of an object.

  Args:
      obj: The object to be inspected.

  Returns:
      A list containing both attributes and methods of the object.
  """
  attributes = dir(obj)
  methods = [method for method in attributes if callable(getattr(obj, method))]
  return attributes + methods

# Example usage
class MyClass:
  def __init__(self, name):
    self.name = name

  def say_hello(self):
    print(f"Hello from {self.name}!")

obj = MyClass("John")

available_elements = lookup(obj)

print(f"Available elements for object {obj}: {available_elements}")
