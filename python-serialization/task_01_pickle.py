import pickle

class CustomObject:
    """Custom class with name, age and is_student."""

    def __init__(self, name, age, is_student):
        """Initialize a CustomObject.

        Args:
            name (str): Name
            age (int): Age
            is_student (bool): Student status
        """
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Display attributs to specified format."""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """Serialize instance to pickle file.

        Args:
            filename (str): Output pickle filename

        Returns:
            bool: True on success, None on error
        """
        try:
            with open(filename, 'wb') as f:
                pickle.dump(self, f)
            return True
        except Exception:
            return None

    @classmethod
    def deserialize(cls, filename):
        """Deserialize pickle file to CustomObject.

        Args:
            filename (str): Input pickle filename

        Returns:
            CustomObject: Instance or None on error
        """
        try:
            with open(filename, 'rb') as f:
                return pickle.load(f)
        except Exception:
            return None
