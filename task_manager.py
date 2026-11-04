"""Command-line task manager with JSON persistence."""
import json
from pathlib import Path

DATA_FILE = Path(__file__).with_name("tasks.json")

def load_tasks():
    """Load tasks, or return an empty list if no saved file exists."""
    if not DATA_FILE.exists():
        return []
    try:
        with DATA_FILE.open("r", encoding="utf-8") as f:
            tasks = json.load(f)
        if not isinstance(tasks, list):
            raise ValueError("Task data must be a list")
        return tasks
    except (json.JSONDecodeError, OSError, ValueError) as error:
        print(f"Could not read saved tasks ({error}). Starting empty.")
        return []

def save_tasks(tasks):
    with DATA_FILE.open("w", encoding="utf-8") as f:
        json.dump(tasks, f, indent=2)

def list_tasks(tasks):
    if not tasks:
        print("No tasks yet.")
    for task in tasks:
        mark = "✓" if task["completed"] else " "
        print(f'{task["id"]}. [{mark}] {task["title"]}')

def add_task(tasks):
    title = input("Task title: ").strip()
    if not title:
        print("Task title cannot be blank.")
        return
    task_id = max((t["id"] for t in tasks), default=0) + 1
    tasks.append({"id": task_id, "title": title, "completed": False})
    save_tasks(tasks)
    print(f"Added task #{task_id}.")

def find_task(tasks, raw_id):
    try:
        task_id = int(raw_id)
    except ValueError:
        print("Please enter a numeric task ID.")
        return None
    for task in tasks:
        if task["id"] == task_id:
            return task
    print("Task ID not found.")
    return None

def complete_task(tasks):
    task = find_task(tasks, input("Task ID to complete: ").strip())
    if task:
        task["completed"] = True
        save_tasks(tasks)
        print("Task marked complete.")

def delete_task(tasks):
    task = find_task(tasks, input("Task ID to delete: ").strip())
    if task:
        tasks.remove(task)
        save_tasks(tasks)
        print("Task deleted.")

def main():
    tasks = load_tasks()
    actions = {"1": lambda: list_tasks(tasks), "2": lambda: add_task(tasks),
               "3": lambda: complete_task(tasks), "4": lambda: delete_task(tasks)}
    while True:
        print("\nTASK MANAGER\n1. List tasks\n2. Add task\n3. Complete task\n4. Delete task\n5. Exit")
        choice = input("Choose an option: ").strip()
        if choice == "5":
            print("Goodbye!")
            break
        action = actions.get(choice)
        if action:
            action()
        else:
            print("Choose a number from 1 to 5.")

if __name__ == "__main__":
    main()
