''' Project 7: Student Management System
Scenario:
A school wants a system to manage student records.
Required Features: - Add student - View students - Update student - Delete student - Store data in file
'''

# File name where all student records will be saved
studentDetail = "studentsDetail.txt"

# Global dictionary to store student data in memory
# Format: { "name": [Id, address, semester, department] }
student = { }


# ADD Student Function
def addStudent():
    # Add a new student record to the system.
    print("=== Add Student ===")

    # Validate: name cannot be empty
    name = input("Enter Name: ")
    if name == "":
        print("Name cannot be empty!")
        return
    
    # Validate: prevent duplicate student names
    if name in student:
        print("Student already Exist!")
        return 

    Id = input("Enter ID No: ")
    address = input("Enter Address: ")
    sem = input("Enter Semester: ")
    department = input("Enter department: ")

    # Store student details as a list with name as key
    student[name] = [Id, address, sem, department]

    # Save updated data to file
    saveToFile()
    
    print("\nThe Student added successfully!")


# Save to File Function
def saveToFile():
    """Save all student records from memory to the text file.
    Each student is written as a comma-separated line.
    Format: name,Id,address,semester,department
    """
    # Open file in write mode (overwrites existing content)
    file = open(studentDetail, "w")

    for name, detail in student.items():
        # Join all fields with comma and add newline at end
        line = name + "," + detail[0] + "," + detail[1]+ "," + detail[2]+ "," + detail[3] + "\n"
        file.write(line)
    file.close()


# Load From file Function
def loadFromFile():
    """Load student records from text file into memory on program startup.
    Handles missing file gracefully if running for the first time.
    """
    try:
        file = open(studentDetail, "r")

        for line in file:
            # Remove newline and split by comma
            parts = line.strip().split(",")

            # Skip incomplete or corrupted lines
            if len(parts) < 5:
                continue
            
            # First part is name (key), rest is the details list
            name = parts[0]
            student[name] = [parts[1], parts[2], parts[3], parts[4]]
        file.close()

    except FileNotFoundError:
        # File doesn't exist yet (first run) — start with empty dict
        pass


# View Student Function
def viewStudents():
    """Display all student records stored in memory."""

    # Check if no students exist
    if len(student) == 0:
        print("No Students Found")
    else:
        print("======== All Students ========")
        for name, detail in student.items():
            # Print each student's details in a readable format
            print(f"Name       : {name}\nID         : {detail[0]}\nAddress    : {detail[1]}\nSemester   : {detail[2]}\nDepartment : {detail[3]}")
            print("----------------------------------")
        

# Update Student Function
def updateStudent():
    """Update a specific field of an existing student record."""

    name = input("Enter student name: ")

    # Check if student exists
    if name not in student:
        print("Student Not found!")
        return
    
    print("======== Update Student Detail ========")
    option = input("What you want to update: \n1. name\n2. ID\n3. Address\n4. Semester\n5. Department: ")

    if option == '1':
        newName = input("Enter New Name: ")
        # Create new key with old value, then delete old key
        # (dict keys cannot be renamed directly)
        student[newName] = student[name]
        del student[name]
        saveToFile()

        print("The name Change successfully!")

    elif option == '2':
        newID = input("Enter New ID: ")
        student[name][0] = newID # index 0 = ID
        saveToFile()

        print("The ID update successfully!")

    elif option == '3':
        newAddress = input("Enter New Address: ")
        student[name][1] = newAddress # index 1 = address
        saveToFile()

        print("The Address update successfully!")

    elif option == '4':
        newSem = input("Enter Semester: ")
        student[name][2] = newSem # index 2 = semester
        saveToFile()

        print("The Semester update successfully!")

    elif option == '5':
        newDepart = input("Enter Department: ")
        student[name][3] = newDepart # index 3 = department
        saveToFile()

        print("The Department update successfully!")

    else: 
        print("Invalid Input!")


# Delete Student Fuction 
def deleteStudent():
    """Delete a student record from memory and update the file."""

    name = input("Enter name: ")
    
    # Check if student exists before deleting
    if name not in student:
        print("The student not found!")
        return 
    
    del student[name] # Remove from dictionary
    saveToFile()      # Update file after deletion

    print("The student delete Successfully!")


# Main Function
def main():
    """Main function — entry point of the program."""

    # Load existing records from file before showing menu
    loadFromFile()

    while(True):
        print("="*6, "Student Management System", "="*6)

        option = input("Enter choice: \n1. Add Student\n2. View Students\n3. Update Student\n4. Delete Student\n5. quit: ")

        if (option == '1'):
            addStudent()
        elif (option == '2'):
            viewStudents()
        elif (option == '3'):
            updateStudent()
        elif (option == '4'):
            deleteStudent()
        elif (option == '5'):
            print("Thank you for using!")
            break # Exit the loop and end program
        else: 
            print("Invalid Input!")

# Program starts here
main()
