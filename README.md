Command-Line Task Manager: A Python program for managing a to-do list from the terminal. Tasks are saved to a file, so they are still there the next time you run it.

Features
Add new tasks
Complete tasks when they are done
Delete tasks you no longer need
List all tasks and their status
Saves automatically to a file so tasks carry over between uses
Input validation so invalid entries (for example, a task number that doesn't exist) show a helpful message instead of crashing

How to Run
Install Python 3.
Download or clone this repository.
In a terminal, go to the project folder and run:
python [your_file_name].py

How It Works
Functions break the program into small, reusable pieces (one for each action).
Lists and dictionaries store each task and its details, such as its description and whether it is complete.
File handling reads tasks when the program starts and writes them back after every change. Data is stored in [tasks.json / tasks.txt].
Input validation checks user input before acting on it.

What I Learned
Organizing a program into functions makes it easier to test and change.
Saving data to a file turns a script into something genuinely useful.
Planning for bad input early prevents most bugs.

Ideas for Next Steps
Add due dates and priority levels
Sort and filter tasks
Edit an existing task
Add automated tests

Author: Pihu Sahai, Computer Science student, University of Michigan
