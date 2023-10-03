import bcrypt


def hash_password(password: str) -> bytes:
    """Hashes a password using bcrypt.

  Args:
    password: The password to hash.

  Returns:
    A hashed password.
  """

    salt = bcrypt.gensalt()
    return bcrypt.hashpw(bytes(password, "utf-8"), salt)


def verify_password(password: str, hashed_password: bytes) -> bool:
    """Verifies a password against a hashed password.

  Args:
    password: The password to verify.
    hashed_password: The hashed password to verify against.

  Returns:
    True if the password is correct, False otherwise.
  """
    return bcrypt.checkpw(bytes(password, "utf-8"), hashed_password)
