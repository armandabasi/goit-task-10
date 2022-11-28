from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value
        

class Name(Field):
    pass


class Phone(Field):
    pass


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        
    def add_phones(self, phone):
        self.phones.append(Phone(phone))

    def get_phones_str(self):
        phone_str = []
        for phone in self.phones:
            phone_str.append(phone.value)
        return phone_str


    def get_phones(self):
        return ", ".join(self.get_phones_str())
    
     
    def delete_phone(self, phone):
        for remove_phone in self.phones:
                if phone == remove_phone.value:
                    self.phones.remove(remove_phone)

    def find_phone(self, phones):
        for phone in phones: 
            if phone not in self.get_phones_str():
                return False
        return True

        

class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record
        
    def show_all_book(self):
        return self.data
        
    def delete_record(self, name):
        del self.data[name]
