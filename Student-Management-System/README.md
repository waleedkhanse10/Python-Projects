## Student Management System
A simple console-based Student Management System built in Python.
It allows users to add, view, update, and delete student records — with data stored in a text file for persistence.

### Features

- ➕ Add Student — Add a new student with Name, ID, Address, Semester, and Department
- 👁️ View Students — Display all stored student records
- ✏️ Update Student — Modify any field of an existing student
- 🗑️ Delete Student — Remove a student record permanently
- 💾 File Storage — All data is saved in a .txt file and loaded on startup


### Project Structure
    project7/
    │
    ├── main.py               # Main program file
    └── studentsDetail.txt    # Auto-generated data file

### How to Run:
- Requirements: Python 3
``` python StudentmanagementSystem.py ```

### Menu
``` 
====== Student Management System ======
Enter choice:
1. Add Student
2. View Students
3. Update Student
4. Delete Student
5. Quit

```

### Data Storage Format
``` Student records are stored in studentsDetail.txt as comma-separated values:
Name,ID,Address,Semester,Department
Ali,101,Lahore,3rd,CS
Sara,102,Karachi,2nd,IT
```

### Functions
```
FunctionDescription:
- addStudent() Takes input and adds student to dict and file
- iewStudents()Displays all student records
- updateStudent() Updates a specific field of a student 
- deleteStudent()Deletes a student by name
- saveToFile()Writes all records to .txt file
- loadFromFile()Loads records from .txt file on startup
```

### Validations
- Empty name not allowed
- Duplicate student name not allowed
- Student not found error on update/delete
- Handles missing file on first run (FileNotFoundError)
- Skips incomplete/corrupted lines in file


### Author
**Waleed Khan**
**BS Software Engineering**