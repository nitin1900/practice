// The Universal JavaScript Formula: Trigger ➔ Data ➔ Screen
// 1. TRIGGER:  What does the human touch? (Click? Type? Submit?)
// 2. DATA:     What information do we need to grab? (Input text? Which button was clicked?)
// 3. SCREEN:   What should physically change on the page? (Add a box? Remove a box? Add a class?)

const taskInput = document.getElementById("task-input");
const addBtn = document.getElementById("add-btn");
const taskList = document.getElementById("task-list");
const checkbox = document.querySelector(".subscribe");
const label = document.querySelectorAll("label");

checkbox.addEventListener("click", () => {
  // .toggle() means: if it doesn't have the class, ADD it. If it has it, REMOVE it!
  label.classList.toggle("completed");
});

// 1. Add a new task section
addBtn.addEventListener("click", () => {
  const taskText = taskInput.value.trim();

  // Prevent adding empty tasks
  if (taskText === "") return;

  // Create the <section class="task">
  const section = document.createElement("section");
  section.className = "task";

  // Create the <label> and <input type="checkbox">
  const label = document.createElement("label");
  const checkbox = document.createElement("input");
  checkbox.type = "checkbox";
  checkbox.className = "subscribe";

  // Put checkbox and text inside the label
  label.append(checkbox, ` ${taskText}`);

  // Create the Delete button
  const deleteBtn = document.createElement("button");
  deleteBtn.className = "delete-btn";
  deleteBtn.textContent = "Delete Task";

  // Assemble the section and add it to the page
  section.append(label, deleteBtn);
  taskList.append(section);

  // Clear the input field
  taskInput.value = "";
});

// 2. Delete any task section (works for existing and new tasks)

// taskList.addEventListener("click", (event) => {
//   if (event.target.classList.contains("delete-btn")) {
//     const sectionToRemove = event.target.closest(".task");
//     sectionToRemove.remove();
//   }
// });

taskList.addEventListener("click", (event) => {
  // 1. If Delete button was clicked
  if (event.target.classList.contains("delete-btn")) {
    const sectionToRemove = event.target.closest(".task");
    sectionToRemove.remove();
  }
  // 2. If Checkbox was clicked
  if (event.target.type === "checkbox") {
    const label = event.target.closest("label");
    label.classList.toggle("completed");
  }
});
