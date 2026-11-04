# command-line-task-manager
Python app to add, complete, delete, and list tasks saved to a file
Command-Line Task Manager (Python)
A menu-driven command-line app to add, list, complete, and delete tasks. Data persists in tasks.json.
Run
Requires Python 3.9+ and no third-party packages. In a terminal opened in this folder:
python task_manager.py
On some systems, use python3 task_manager.py.
Features
Functions split into focused responsibilities
Lists and dictionaries for task data
JSON file persistence
Validation for blank titles and invalid IDs
Handles missing or malformed saved data
Try
List sample tasks.
Add a task, then list it.
Try a blank title.
Complete a task and restart the program.
Try a non-numeric ID and a nonexistent ID.
Design choices
JSON is human-readable and available in Python's standard library. Functions separate persistence, lookup, user input, and the menu. Possible extensions: due dates, priorities, search, unit tests, and backup files.
testing/validations
result sets
