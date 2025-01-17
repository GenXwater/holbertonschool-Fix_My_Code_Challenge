#!/usr/bin/python3
"""
User Model with Unique ID and Secure Password Handling
"""
import hashlib
import uuid


class User:
    """
    User class:
    - id: Public unique string (UUID)
    - password: Private hashed string using MD5
    """
    def __init__(self):
        """
        Initializes a new User instance:
        - Assigns a unique `id`
        - Sets the initial `__password` to None
        """
        self.id = str(uuid.uuid4())
        self.__password = None

    @property
    def password(self):
        """
        Getter for password:
        - Returns the hashed password
        """
        return self.__password

    @password.setter
    def password(self, pwd):
        """
        Setter for password:
        - Sets `__password` to None if `pwd` is None or not a string
        - Otherwise, hashes the `pwd` using MD5 and stores the hash
        """
        if not isinstance(pwd, str):
            self.__password = None
        else:
            self.__password = hashlib.md5(pwd.encode()).hexdigest()

    def is_valid_password(self, pwd):
        """
        Validates the given password against the stored hash:
        - Returns False if `pwd` is None, not a string, or if `__password` is None
        - Compares the MD5 hash of `pwd` with the stored hash
        """
        if not isinstance(pwd, str) or self.__password is None:
            return False
        return hashlib.md5(pwd.encode()).hexdigest() == self.__password


if __name__ == '__main__':
    print("Testing User class functionality...")

    # Test unique ID generation
    user1 = User()
    user2 = User()
    if user1.id == user2.id:
        print("Error: User IDs should be unique.")

    # Test password setting and hashing
    test_password = "SecurePassword123"
    user1.password = test_password
    if user1.password == test_password:
        print("Error: Password should be stored as a hash, not plain text.")

    # Test default password state
    if user2.password is not None:
        print("Error: Password should default to None for new users.")

    # Test invalid password assignments
    user2.password = None
    if user2.password is not None:
        print("Error: Password should remain None when set to None.")

    user2.password = 12345
    if user2.password is not None:
        print("Error: Password should remain None when set to a non-string value.")

    # Test password validation
    if not user1.is_valid_password(test_password):
        print("Error: is_valid_password should return True for a correct password.")

    if user1.is_valid_password("WrongPassword"):
        print("Error: is_valid_password should return False for an incorrect password.")

    if user1.is_valid_password(None):
        print("Error: is_valid_password should return False when given None.")

    if user1.is_valid_password(12345):
        print("Error: is_valid_password should return False when given a non-string value.")

    if user2.is_valid_password("NoPasswordSet"):
        print("Error: is_valid_password should return False if no password has been set.")
