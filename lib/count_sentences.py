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

    def count_sentences(self):
        if self._value is None:
            return 0

        # Heuristic: Count sentences based on common punctuation marks
        sentence_endings = ['.', '!', '?']
        count = sum(1 for char in self._value if char in sentence_endings)

        return count

# Example usage:
my_str_instance = MyString()
my_str_instance.value = "Hello! How are you? This is an example sentence."

sentence_count = my_str_instance.count_sentences()
print(f"Number of sentences: {sentence_count}")  # Output: Number of sentences: 3
