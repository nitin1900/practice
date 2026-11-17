// Golden rule: TRIGGER -> DATA -> SCREEN

//add the task

const input = document.querySelector("#task-input");
const add = document.querySelector("#add-btn");
const taskList = document.querySelector("#task-list");
const deleteBtn = document.querySelector(".delete-btn");

add.addEventListener("click", () => {
  if (!input.value.trim()) {
    return;
  }
  //section created
  const section = document.createElement("section");
  section.className = "task";

  //checkbox created
  const checkbox = document.createElement("input");
  checkbox.type = "checkbox";

  // label created
  const label = document.createElement("label");

  //trying to create delete button
  const button = document.createElement("button");
  button.textContent = "Delete Task";
  button.className = "delete-btn";

  //attaching together
  label.append(checkbox, "", input.value);

  section.append(label, button);

  //to display in the screen and empty the input for next...
  taskList.append(section);
  input.value = "";
});

taskList.addEventListener("click", () => {
  //making the line-through work
  if (event.target.type === "checkbox") {
    const label = event.target.closest("label");
    label.classList.toggle("completed");
  }

  //making the delete button work
  if (event.target.classList.contains("delete-btn")) {
    const task = event.target.closest(".task");
    task.remove();
  }
  // these two above if satement are liitle hard to digest...
});

//feature wanted to add is that
// 1. at the starting always the checkpoint should be un tick
// 2. when give the input in box then i don't explicity press add task instead i can press enter and all done same as pressing the add task button
