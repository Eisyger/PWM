import unittest
import random
import string
from restrictions import Restrictions


class TestUsernameValidation(unittest.TestCase):

    def test_valid_username(self):
        self.assertTrue(Restrictions.check_username("valid123"))

    def test_short_username(self):
        self.assertFalse(Restrictions.check_username("sh"))

    def test_long_username(self):
        self.assertFalse(Restrictions.check_username("this_is_a_very_long_username"))

    def test_invalid_characters(self):
        self.assertFalse(Restrictions.check_username("invalid@username"))

    def test_valid_mixed_case_username(self):
        self.assertTrue(Restrictions.check_username("MixedCase123"))

    def test_random_username(self):
        random_username = ''.join(
            random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789') for _ in range(15))
        self.assertTrue(Restrictions.check_username(random_username))


class TestCheckPasswordMethod(unittest.TestCase):

    def test_valid_password(self):
        result = Restrictions.check_password("StarkesPasswort1!")
        self.assertTrue(result)

    def test_invalid_short_password(self):
        result = Restrictions.check_password("Kurz1!")
        self.assertFalse(result)

    def test_invalid_no_uppercase(self):
        result = Restrictions.check_password("passwort1!")
        self.assertFalse(result)

    def test_random_password(self):
        # Generiere ein zufälliges Passwort
        random_password = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=15))
        print("Zufälliges Passwort:", random_password)

        result = Restrictions.check_password(random_password)
        self.assertTrue(result)


if __name__ == '__main__':
    unittest.main()
