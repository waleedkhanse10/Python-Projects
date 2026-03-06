## Contact Management System.
A simple command-line Contact Manager built in Python.
Allows users to add, search, update, delete, and view contacts — with data saved permanently to a file.

### Features:
- ➕ Add a new contact (name + phone number)
- 🔍 Search contact by name
- ✏️ Update an existing contact's number
- 🗑️ Delete a contact
- 📋 View all saved contacts
- 💾 Data is saved to a .txt file — contacts are not lost when you close the program

### Built With:
- **Python 3**.
- **Concepts used**: Dictionaries, Functions, File Handling, Loops, Conditionals

### Project Structure
    contact-book/
    │
    ├── main.py          # Main source code
    ├── contacts.txt     # Auto-generated file where contacts are saved
    └── README.md        # Project documentation

### How to Run:
1. Make sure Python 3 is installed on your system
2. Clone or download this repository
3. Open terminal in the project folder
4. Run the program:
`python main.py`

### How It Works
```======= Contact Manager =======
Enter What you want:
```
1. Add Contact
2. Search Contact
3. Update Contact
4. Delete Contact
5. Show Contacts
6. Quit

- Contacts are stored in memory using a dictionary
- On startup, existing contacts are loaded from contacts.txt
- Any add/update/delete operation is instantly saved back to the file
- Names are stored in UPPERCASE to avoid duplicate entries

### What I Learned:
- How to use Python dictionaries to store key-value data
- Reading and writing files using open(), readlines(), and write()
- Organizing code into clean, reusable functions
- Handling edge cases like duplicate contacts and missing files (FileNotFoundError)

### Future Improvements:
- Add phone number validation
- Support multiple numbers per contact
- Add a GUI using Tkinter
- Store data in JSON format instead of plain text

**Part of my Python Projects collection** 