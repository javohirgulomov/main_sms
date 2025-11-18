import re

s=r'^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$'

class Contact:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone


class ContactManager:
    def __init__(self):
        self.contacts = []

    def add_contacts(self):
        name = input("Enter your name: ")
        while True:
            phone = input("Enter your phone: ")
            if re.match(s, phone):
                break
            else:
                print("Xato raqam! Qaytadan kiriting.")

        c = Contact(name, phone)
        self.contacts.append(c)
        print("Contact Added")

    def find_contact(self, phone):
        for c in self.contacts:
            if c.phone == phone:
                return True
        return False

    def list_contacts(self):
        if not self.contacts:
            print("No contacts yet")
            return
        for i in self.contacts:
            print(f'name: {i.name} number: {i.phone}')


class SMS:
    def __init__(self, sender, receiver, text):
        self.sender = sender
        self.receiver = receiver
        self.text = text


class SMSManager:
    def __init__(self, contact_manager: ContactManager):
        self.sms_list = []
        self.contact_manager = contact_manager

    def send_Sms(self):
        sender = input("Input your number: ")
        receiver = input("Input receiver phone number: ")
        if not self.contact_manager.find_contact(receiver):
            print("Phone number not found")
            return
        text = input("Input your text: ")

        s = SMS(sender, receiver, text)
        self.sms_list.append(s)
        print("Sms Sent")

    def view_sms(self):
        if not self.sms_list:
            print("No sms sent yet")
            return
        for s in self.sms_list:
            print(f'name: {s.sender} number: {s.receiver} text: {s.text}')

def pro_manager():
    cm = ContactManager()
    sm = SMSManager(cm)
    while True:
        print(" 1.Add contact \n 2.View Contacts \n 3.Send SMS \n 4. View SMS \n 5.Exit \n")
        choice = input("Enter your choice: ")
        if choice == '1':
            cm.add_contacts()
        elif choice == '2':
            cm.list_contacts()
        elif choice == '3':
            sm.send_Sms()
        elif choice == '4':
            sm.view_sms()
        elif choice == '5':
            break
        else:
            print("Invalid")

pro_manager()