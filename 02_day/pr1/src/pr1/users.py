def login(username: str, password: str) -> bool:
    """
    Simple login function that checks against static credentials.
    Returns True if login is successful, False otherwise.
    """
    return username == "admin" and password == "admin"

def signup(username: str, password: str) -> bool:
    """
    Simple signup function that only allows creating an admin account if it doesn't exist.
    Since we're using static credentials, this will always return False as the admin
    account is pre-defined.
    """
    # Since we're using static credentials, signup is not really applicable
    # Always return False as we don't allow new user creation in this simple version
    return False
