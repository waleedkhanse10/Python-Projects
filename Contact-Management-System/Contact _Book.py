'''Project 6: Contact Book
# Scenario: A mobile user wants a simple contact manager. Required Features: - Add contact - Search contact - Update contact - Delete contact .Concepts Practiced: - dictionaries - functions - file handling'''

# Contact Dictionary
contacts = {}

# save in file
contactsFile = "contacts.txt"

# Load file into dictionary at start
try:
    with open("contacts.txt" , "r") as file:
        read = file.readlines()
        for line in read:
            name, phoneNO = line.strip().split(",")
            # load to dictionary
            contacts[name.upper()] = phoneNO

except FileNotFoundError:
    pass # file doesn't exist yet, start with empty dictionary

# add contact
def addContact():
    print("======= Add Contact =======")
    name = input("Enter name: ")

    if name.upper() in contacts:
        print("The name already exist")
        return
    
    phoneNO = input("Enter Contact: ")
    contacts[name.upper()] = phoneNO

    with open("contacts.txt", "a") as file:
        file.write(f"{name.upper()},{phoneNO}\n")

    print("Contact Added Successfully!")

# View all  contact
def viewContacts():
    print("======= Contact List =======")

    if len(contacts) == 0:
        print("Contact List Empty!")

    for name, phoneNO in contacts.items():
        print(f"Name: {name}\nContact No: {phoneNO}")
    
# search contact by name
def searchContact():
    print("======= Search Contact =======")

    name = input("Enter Name: ")

    if name.upper() in contacts:
        print(f"{name.upper()} = {contacts[name.upper()]}")
    else:
        print("Contact Not found!")

# write the contact back to contacts.txt
def writeBack():
    with open("contacts.txt", "w") as file:
        for i,j in contacts.items():
            file.write(f"{i},{j}\n")

# update contact
def updateContact():
    print("======= Update Contact =======")

    name = input("Enter name: ")

    if name.upper() in contacts:
        newNo = input("Enter New Number: ")
        contacts[name.upper()] = newNo
        print("The Number Update Successfully!")
        writeBack()
    else:
        print("The name not found!")
    

def deleteContact():
    print("======= Delete Contact =======")

    name = input("Enter Name: ")

    if name.upper() in contacts:
        del contacts[name.upper()]
        print("The Number delete Successfully!")
        writeBack()
    else:
        print("Number Not Found!")

def main():
    while True:
        print("======= Contact Manager =======")
        choice = input("Entet What you want \n1. Add Contact\n2. Search Contact\n3. Update Contact\n4. Delete Contact\n5. Show Contacts\n6. Quite: ")

        if choice == "1":
            addContact()

        elif choice == "2":
            searchContact()

        elif choice == "3":
            updateContact()

        elif choice == "4":
            deleteContact()

        elif choice == "5":
            viewContacts()

        elif choice == "6":
            print("Thank you for using!")
            break
        else:
            print("Invalid Input!")

main()