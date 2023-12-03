#!/usr/bin/env python3

class MyString:
    def __init__(self):
        self._value = None  # Initialize value to None

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        if not isinstance(new_value, str):
            print("Value must be a string.")
        else:
            self._value = new_value

# Example usage:
my_str_instance = MyString()

my_str_instance.value = "Hello, World!"  # Valid string
print(my_str_instance.value)  # Output: Hello, World!

my_str_instance.value = 42  # Invalid value (not a string)
# Output: Value must be a string.
