import re
import unittest

class DataValidator:
    def email(self, data):
        # Checks weather the email is valid
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+(?:\.[a-zA-Z]{2,}|(?:\d{1,3}\.){3}\d{1,3})$'
        return bool(re.fullmatch(pattern, data))


    def phone(self, data):
        # Checks weather the number is a valid UK phone number
        pattern = r'^(((\+44\s?\d{4}|\(?0\d{4}\)?)\s?\d{3}\s?\d{3})|((\+44\s?\d{3}|\(?0\d{3}\)?)\s?\d{3}\s?\d{4})|((\+44\s?\d{2}|\(?0\d{2}\)?)\s?\d{4}\s?\d{4}))(\s?\#(\d{4}|\d{3}))?$'
        return bool(re.fullmatch(pattern, data))


    def name(self, data):
        if re.match(r'^[a-zA-Z]+$', data):
            return True
        return False


    def username(self, data):
        if re.match(r'^[a-zA-Z0-9]+$', data):
            return True
        return False


    def birthdate(self, data):
        if re.match(r'^\d{4}-\d{2}-\d{2}$', data):
            return True
        return False


    def age(self, data):
        if re.match(r'^[0-9]+$', data) and 0 < int(data) < 150:
            return True
        return False


    def length_check(self, data, length, option):
        if option == 'min':
            if len(data) >= length:
                return True
        elif option == 'max':
            if len(data) <= length:
                return True
        elif option == 'equal':
            if len(data) == length:
                return True
        return False

class TestValidator(unittest.TestCase):
    def setUp(self):
        # Create an instance of the DataValidator class to test data validation
        self.validator = DataValidator()

    def test_valid_email(self):
        # Valid emails
        valid_emails = [
        'user@example.com',
        'email@example.co.jp',
        'firstname-lastname@example.com',
        'email@example.museum',
        'email@example.name',
        '_______@example.com',
        '1234567890@example.com',
        'email@123.123.123.123'
        ]

        for email in valid_emails:
            # Tests valid emails
            self.assertTrue(self.validator.email(email))


    def test_invalid_email(self):
        # Invalid emails
        invalid_emails = [
        'plainaddress',
        '@example.com',
        'email@',
        'email@.com',
        'email@'
        ]

        for email in invalid_emails:
            # Tests invalid emails
            self.assertFalse(self.validator.email(email))


    def test_valid_phone(self):
        # Valid phone numbers
        valid_phones = [
        '+44 7975 556677',
        '07947674716',
        '020 7946 0716',
        '02079460716',
        '07975 556677'
]

        for phone in valid_phones:
            # Tests valid phone numbers
            self.assertTrue(self.validator.phone(phone))


    def test_invalid_phone(self):
        # Invalid phone numbers
        invalid_phones = [
        '1234567890',
        '1234',
        '12345678901234567890',
        '1234567890',
        '+1234567890',
        '+44 1234 56789',
]

        for phone in invalid_phones:
            # Tests invalid phone numbers
            self.assertFalse(self.validator.phone(phone))


if __name__ == '__main__':
    unittest.main()
