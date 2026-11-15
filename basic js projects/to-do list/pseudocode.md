HTML:
create text input field for entering task
create button to add the task
create container (main or ul) to hold dynamic task list
link style.css in head and script.js at end of body

CSS:
basic reset and layout styling
style input field and add button
style each task row - align checkbox, task text, and delete button
define default task text state - text-decoration none
define completed task text state - text-decoration line-through, faded color
style delete button

JAVASCRIPT:
select input field, add button, and task list container from DOM
listen for click event on add button
get text from input field and trim whitespace
validation - check if empty, return if true
create task row element (section or li)
create checkbox element
create label element with task text and checkbox inside
create delete button element
assemble row - append label and delete button into task row
append task row to main task list container on page
clear input field
listen for click events on main task list container (event delegation)
check if delete button clicked - remove closest task row from page
check if checkbox clicked - toggle completed class on closest label
