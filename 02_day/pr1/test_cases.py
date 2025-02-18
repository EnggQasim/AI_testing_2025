```python
import unittest

class TestLoginSignup(unittest.TestCase):

    def test_login_success(self):
        self.assertTrue(login("admin", "admin"))

    def test_login_failure_wrong_username(self):
        self.assertFalse(login("user", "admin"))

    def test_login_failure_wrong_password(self):
        self.assertFalse(login("admin", "user"))

    def test_login_failure_both_wrong(self):
        self.assertFalse(login("user", "user"))

    def test_login_empty_username(self):
        self.assertFalse(login("", "admin"))

    def test_login_empty_password(self):
        self.assertFalse(login("admin", ""))

    def test_login_empty_both(self):
        self.assertFalse(login("", ""))

    def test_signup_always_fails(self):
        self.assertFalse(signup("admin", "admin"))
        self.assertFalse(signup("user", "password"))
        self.assertFalse(signup("", ""))
        self.assertFalse(signup("testuser", "testpassword"))


if __name__ == '__main__':
    unittest.main()
```
