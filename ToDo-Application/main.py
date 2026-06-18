#---------- FILES ----------#
All_Task = "all_tasks.txt"
Complete_Task = "complete_task.txt"

#---------- FUNCTIONS ----------#
def add():
    title = input("Enter Title of Task: ")
    detail = input("Enter Detail: ")
    time = input("Ending Date/time: ")

    with open(All_Task, "a") as file:
        file.write(f"{title}|{detail}|{time}\n")
    print("Task Added Successfully!\n")

#---------- VIEW ----------*
def view():
    print("=" * 40)
    print("         VIEW TASKS  ")
    print("=" * 40)

    try:
        with open(All_Task, "r") as file:
            lines = file.readlines()
            if not lines:
                print("No tasks found!")
            else:
                for i in lines:
                    split = i.strip().split("|")
                    print(f"Title: {split[0]}\nDescription: {split[1]}\nDate/Time: {split[2]}")
                    print("---------------------------------------")
    except FileNotFoundError:
        print("No tasks found!")

#---------- VIEW Detail ----------*
def view_detail():
    print("=" * 40)
    print("         VIEW DETAIL  ")
    print("=" * 40)
    name = input("Enter task name: ")

    try:
        with open(All_Task, "r") as file:
            found = False
            for i in file:
                split = i.strip().split("|")
                if split[0] == name:          # exact match
                    print(f"Title: {split[0]}\nDescription: {split[1]}\nDate/Time: {split[2]}")
                    found = True
                    break
            if not found:
                print("Task Does Not Exist")
    except FileNotFoundError:
        print("No tasks found!")

    print("--------------------------------------")

#---------- DELETE ----------*

def delete():
    print("=" * 40)
    print("         DELETE TASK  ")
    print("=" * 40)

    name = input("Enter the name of Task? ")

    try:
        with open(All_Task, "r") as file:
            read = file.readlines()
    except FileNotFoundError:
        print("No tasks found!")
        return

    with open(All_Task, "w") as file:
        task_deleted = False

        for i in read:
            split = i.strip().split("|")
            if split[0] != name:   # exact match on title only
                file.write(i)
            else:
                task_deleted = True

        if task_deleted:
            print("The task deleted successfully!")
        else:
            print("The task does not exist!")

        print("--------------------------------------")

#---------- UPDATE DETAILS ----------*
def update_detail():
    print("=" * 40)
    print("         UPDATE DETAILS  ")
    print("=" * 40)

    name = input("Enter the Task Name? ")
    try:
        with open(All_Task, "r") as file:
            read = file.readlines()
    except FileNotFoundError:
        print("No tasks found!")
        return

    with open(All_Task, "w") as file:
        found = False
        for i in read:
            split = i.strip().split("|")
            if split[0] == name:              # exact match on title only
                new_title = input("Enter new Title: ")
                new_des = input("Enter new Description: ")
                new_time = input("Enter new Date/Time: ")
                file.write(f"{new_title}|{new_des}|{new_time}\n")
                found = True
            else:
                file.write(i)

        if found:
            print("The Details Were Updated Successfully!")
        else:
            print("Sorry! The Task Does Not Exist")

        print("--------------------------------------")

#---------- COMPLETE TASK ----------*

def complete_task():
    print("=" * 40)
    print("         COMPLETE TASK  ")
    print("=" * 40)
    name = input("Enter the complete task name: ")
    
    with open(All_Task, "r") as file:
        read = file.readlines()

    # Step 1: find task
    found = False
    for i in read:
        split = i.strip().split("|")
        if split[0] == name:          # exact match
            found = True
            break

    if not found:
        print("Task Does Not Exist")
        return

    # Step 2: write in complete_task.txt 
    with open(Complete_Task, "a") as comp_file:
        for i in read:
            split = i.strip().split("|")
            if split[0] == name:
                comp_file.write(f"Title: {split[0]}\nDescription: {split[1]}\nDate/Time: {split[2]}\n----------------------------------------------------\n")


    with open(All_Task, "w") as all_file:
        for i in read:
            split = i.strip().split("|")
            if split[0] != name:      # exact match
                all_file.write(i)

    print("The Task Completed Successfully!")
    print("-----------------------------------------------")

#---------- VIEW COMPLETE TASK ----------*
def view_complete_task():
    print("=" * 40)
    print("         VIEW COMPLETE TASKS  ")
    print("=" * 40)

    try:
        with open(Complete_Task, "r") as file:
            read = file.read()
            if read.strip() == "":
                print("No completed tasks yet!")
            else:
                print(read)
    except FileNotFoundError:
        print("No completed tasks yet!")
        
    print("--------------------------------------")

#---------- MAIN ----------#
print("=" * 40)
print("      ToDo App by Waleed Khan  ")
print("=" * 40)

def main():
    while True:
        choice = input("""Enter Your Choice.
        1. ADD TASK
        2. VIEW TASKS
        3. VIEW SPECIFIC TASK DETAIL
        4. DELETE TASKS
        5. UPDATE Details OF TASKS
        6. COMPLETE TASK
        7. VIEW COMPLETE TASK
        0. CLOSE: """)

        if choice == "1":
            add()
        elif choice == "2":
            view()
        elif choice == "3":
            view_detail()
        elif choice == "4":
            delete()
        elif choice == "5":
            update_detail()
        elif choice == "6":
            complete_task()
        elif choice == "7":
            view_complete_task()
        elif choice == "0":
            print("Thanks! For Using")
            break
        else: 
            print("invalid input!")
main()