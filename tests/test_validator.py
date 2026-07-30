import unittest

from utils.validators import PasswordValidator


class ValidatorTests(unittest.TestCase):

    def test_password(self):

        validator = PasswordValidator()

        self.assertTrue(

            validator.validate(

                "Password123!"

            )

        )


if __name__ == "__main__":

    unittest.main()
