📝 To-Do List — Pseudocode
Phase 1: Basic setup

    Create an input box for the user to enter a task.
    Create an Add button.
    Create an empty container where tasks will appear.
    In JavaScript, select/get access to:
        input
        Add button
        task container

Phase 2: Add a task

When the user clicks Add:

    Get the text from the input.
    Check if the input is empty.
        If empty → show an error / don't add anything.
    Create a new task element.
    Put the entered text inside the task element.
    Add the task element to the task container.
    Clear the input box.

At this point, you should be able to do:

Input: Learn JavaScript

        ↓ Add

Todo list:
- Learn JavaScript

Phase 3: Delete a task

For every task:

    Create a Delete button.
    Put the Delete button next to the task.
    Listen for a click on Delete.
    When clicked:
        Remove that particular task from the page.

Result:

- Learn JavaScript    [Delete]
- Learn HTML          [Delete]

Click Delete on HTML

        ↓

- Learn JavaScript    [Delete]

Phase 4: Complete a task

When the user clicks a task:

    Determine which task was clicked.
    Change its completed state.
    Visually show it as completed.
        Example: strike-through text.
    If clicked again, undo the completed state.

Think:

[ ] Learn JavaScript

↓

[x] Learn JavaScript

↓

click again

[ ] Learn JavaScript

Phase 5: Edit a task

When the user clicks Edit:

    Get the existing task text.
    Put that text into an input field.
    Allow the user to change it.
    When they save:
        Validate the new text.
        Replace the old task text with the new text.

Example:

- Learn Javascrip    [Edit]

↓

- [Learn Javascrip] [Save]

↓

- Learn JavaScript   [Edit]

Phase 6: Search

Create a search input.

When the user types:

    Get the search text.
    Go through every task.
    Compare the search text with the task text.
    If the task matches → show it.
    If it doesn't match → hide it.

Example:

Search: javascript

- Learn JavaScript
- JavaScript DOM
- Learn Python
- Learn Git

↓

- Learn JavaScript
- JavaScript DOM

Phase 7: Store your data

Don't start here. Do this only after the previous parts work.

Instead of thinking:

    "I need to save HTML."

Think:

    "I need to save my tasks as data."

Represent each task as something like:

Task:
    id
    text
    completed

Your application should have a collection of tasks:

tasks
 ├── task 1
 ├── task 2
 ├── task 3
 └── task 4

Whenever the user:

    adds a task
    deletes a task
    edits a task
    completes a task

you should:

1. Change the tasks data
2. Save the updated data to localStorage
3. Update what is displayed on the page

When the page first loads:

Page loads
    ↓
Get saved tasks from localStorage
    ↓
If tasks exist
    ↓
Create/display them

Your final architecture

Eventually, your app should roughly work like this:

                    TODO APP
                       │
          ┌────────────┴────────────┐
          ↓                         ↓
       USER INPUT                STORAGE
          │                         │
          ↓                         ↓
    Add / Edit / Delete        localStorage
    Complete / Search               │
          │                         │
          └──────────┬──────────────┘
                     ↓
                 TASK DATA
                     │
                     ↓
               UPDATE DOM
                     │
                     ↓
                SCREEN

Your challenge 🎯

Don't try to build everything.

Start with only this pseudocode:

1. Get input
2. Get Add button
3. Get task container

4. When Add is clicked:
      get input text
      check if empty
      create task
      put text in task
      add task to container
      clear input