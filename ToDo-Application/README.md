# 📝 ToDo App

A simple command-line ToDo application built with Python. It allows you to manage your tasks — add, view, update, delete, and mark them as complete — all stored in local text files.

---

## Features

- Add new tasks with title, description, and due date
- View all tasks
- View a specific task by name
- Update task details
- Delete a task
- Mark a task as complete (moves it to a completed list)
- View all completed tasks

---

## How to Run

**Requirements:** Python 3.x

```bash
python main.py
```

No external libraries needed — uses Python built-ins only.

---

## Usage

Once you run the program, a menu will appear:

```
1. ADD TASK
2. VIEW TASKS
3. VIEW SPECIFIC TASK DETAIL
4. DELETE TASKS
5. UPDATE Details OF TASKS
6. COMPLETE TASK
7. VIEW COMPLETE TASK
0. CLOSE
```

Enter the number of your choice and follow the prompts.

---

## File Structure

```
Todo-App/
├── main.py            # Main application
├── all_tasks.txt      # Auto-created — stores active tasks
├── complete_task.txt  # Auto-created — stores completed tasks
└── README.md
```

> `all_tasks.txt` and `complete_task.txt` are created automatically when you first use the app.

---

## Author

**Waleed Khan** — [GitHub](https://github.com/waleedkhanse10)
