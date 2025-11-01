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


