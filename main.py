from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    pass

class Phone(Field):
    def __init__(self, value):
        if not (len(value) == 10 and value.isdigit()):
            raise ValueError("Phone number must be 10 digits.")
        super().__init__(value)

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone_str):
        phone = Phone(phone_str)
        self.phones.append(phone)

    def remove_phone(self, phone_str):
        phone_obj = self.find_phone(phone_str)
        if phone_obj:
            self.phones.remove(phone_obj)
        else:
            raise ValueError(f"Phone {phone_str} not found.")

    def edit_phone(self, old_phone_str, new_phone_str):
        for i, phone_obj in enumerate(self.phones):
            if phone_obj.value == old_phone_str:
                self.phones[i] = Phone(new_phone_str)
                return
        raise ValueError(f"Phone {old_phone_str} not found.")

    def find_phone(self, phone_str):
        for phone_obj in self.phones:
            if phone_obj.value == phone_str:
                return phone_obj
        return None

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"


class AddressBook(UserDict):
    
    def add_record(self, record: Record):
        self.data[record.name.value] = record

    def find(self, name):
        return self.data.get(name)

    def delete(self, name):
        if name in self.data:
            self.data.pop(name)
        else:
            raise KeyError(f"Contact {name} not found.")

if __name__ == "__main__":
    try:
        # Create a new AddressBook
        book = AddressBook()

        # Create a Record for John
        john_record = Record("John")
        john_record.add_phone("1234567890")
        john_record.add_phone("5555555555")

        # Add Record for John
        book.add_record(john_record)

        # Create and add Record for Jane
        jane_record = Record("Jane")
        jane_record.add_phone("9876543210")
        book.add_record(jane_record)

        # Print all Records
        print("All records:")
        for name, record in book.data.items():
            print(record)

        # Find and update phone for John
        john = book.find("John")
        john.edit_phone("1234567890", "1112223333")

        print(f"\nUpdated John: {john}")  # Contact name: John, phones: 1112223333; 5555555555

        # Find a valid phone of John
        found_phone = john.find_phone("5555555555")
        print(f"\nFound phone for {john.name.value}: {found_phone.value}")  # Виведення: 5555555555

        # Delete record for Jane
        book.delete("Jane")
        print("\nAll records after deleting Jane:")
        for name, record in book.data.items():
            print(record)

        # Test wrong data
        try:
            john.add_phone("123")
        except ValueError as e:
            print(f"\nValidation error: {e}")

    except (ValueError, KeyError, AttributeError) as e:
        print(f"An error occurred: {e}")

