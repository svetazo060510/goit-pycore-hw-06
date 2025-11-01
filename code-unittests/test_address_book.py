# Run from terminal
# python3 -m unittest test_address_book.py

import unittest
from main import Field, Name, Phone, Record, AddressBook

class TestAddressBook(unittest.TestCase):
    
    def setUp(self):
        """
        Set up a fresh AddressBook and Records for each test.
        This runs before every 'test_' method.
        """
        self.book = AddressBook()
        self.john_record = Record("John")
        self.john_record.add_phone("1234567890")
        self.john_record.add_phone("5555555555")
        
        self.jane_record = Record("Jane")
        self.jane_record.add_phone("9876543210")

    def test_add_record(self):
        """Test adding a record to the address book."""
        self.book.add_record(self.john_record)
        self.assertIn("John", self.book.data)
        self.assertEqual(self.book.data["John"], self.john_record)

    def test_find_record_found(self):
        """Test finding an existing record."""
        self.book.add_record(self.john_record)
        found_record = self.book.find("John")
        self.assertIsNotNone(found_record)
        self.assertEqual(found_record.name.value, "John")

    def test_find_record_not_found(self):
        """Test finding a non-existent record."""
        found_record = self.book.find("Bill")
        self.assertIsNone(found_record)

    def test_delete_record(self):
        """Test deleting a record from the address book."""
        self.book.add_record(self.john_record)
        self.book.add_record(self.jane_record)
        
        self.book.delete("Jane")
        
        self.assertNotIn("Jane", self.book.data)
        self.assertIn("John", self.book.data)

    def test_add_phone(self):
        """Test adding a phone to a record."""
        # setUp already added two phones
        self.assertEqual(len(self.john_record.phones), 2)
        
        self.john_record.add_phone("1111111111")
        self.assertEqual(len(self.john_record.phones), 3)
        self.assertEqual(self.john_record.phones[-1].value, "1111111111")

    def test_remove_phone(self):
        """Test removing a phone from a record."""
        self.john_record.remove_phone("1234567890")
        self.assertEqual(len(self.john_record.phones), 1)
        self.assertIsNone(self.john_record.find_phone("1234567890"))
        self.assertIsNotNone(self.john_record.find_phone("5555555555"))

    def test_edit_phone(self):
        """Test editing an existing phone number."""
        self.john_record.edit_phone("1234567890", "1112223333")
        
        # Check that the old number is gone
        self.assertIsNone(self.john_record.find_phone("1234567890"))
        
        # Check that the new number exists
        new_phone = self.john_record.find_phone("1112223333")
        self.assertIsNotNone(new_phone)
        self.assertEqual(new_phone.value, "1112223333")

    def test_find_phone_found(self):
        """Test finding an existing phone number."""
        found_phone = self.john_record.find_phone("5555555555")
        self.assertIsNotNone(found_phone)
        self.assertEqual(found_phone.value, "5555555555")

    def test_find_phone_not_found(self):
        """Test finding a non-existent phone number."""
        found_phone = self.john_record.find_phone("0000000000")
        self.assertIsNone(found_phone)

    def test_phone_validation_short(self):
        """Test that Phone validation rejects numbers that are too short."""
        # 'with self.assertRaises(ValueError)' checks that the code inside
        # correctly raises a ValueError.
        with self.assertRaises(ValueError):
            Phone("123")

    def test_phone_validation_long(self):
        """Test that Phone validation rejects numbers that are too long."""
        with self.assertRaises(ValueError):
            Phone("12345678901")
            
    def test_phone_validation_non_digit(self):
        """Test that Phone validation rejects numbers with letters."""
        with self.assertRaises(ValueError):
            Phone("123456789a")

    def test_record_str_representation(self):
        """Test the __str__ method of the Record class."""
        self.assertEqual(str(self.john_record), "Contact name: John, phones: 1234567890; 5555555555")

# This allows the test file to be run directly
if __name__ == '__main__':
    unittest.main()