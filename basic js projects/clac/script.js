/*
1. select elements: display screen and all buttons
2. define state variables: firstNumber, operator, isNewNumber
3. loop through all buttons and add click event listener
4. get clicked button value
5. if AC: reset display to '0' and reset all state variables
6. if number (0-9): replace if display is '0' or isNewNumber is true, else append
7. if operator (+, -, *, /): store firstNumber, store operator, set isNewNumber to true
8. if '=': parse numbers, calculate result based on operator, update display, set isNewNumber to true
9. if '.': handle decimal (prevent multiple dots, handle starting fresh with '0.')
10. if '+/-': toggle positive/negative sign
11. if 'C': backspace / remove last digit
*/

// 1. select elements: display screen and all buttons
const display = document.querySelector(".display"); //not all because there is only one element present
const buttons = document.querySelectorAll("button"); //class is . and id is # and for normal it is tag

// 2. define state variables: firstNumber, operator, isNewNumber
let firstNumber = null;
let operator = "";
let isNewNumber = true;

// 3. loop through all buttons and add click event listener
buttons.forEach((button) => {
  button.addEventListener("click", () => {
    // 4. get clicked button value
    const value = button.innerText;

    // 5. if AC: reset display to '0' and reset all state variables
    if (value === "AC") {
      display.textContent = 0;
      firstNumber = null;
      operator = "";
      isNewNumber = true;
    }

    // 6. if number (0-9): replace if display is '0' or isNewNumber is true, else append
    else if ("0123456789".includes(value)) {
      if (display.textContent === "0" || isNewNumber) {
        display.textContent = value;
        isNewNumber = false;
      } else {
        display.textContent += value;
      }
    }

    // 7. if operator (+, -, *, /): store firstNumber, store operator, set isNewNumber to true
    else if (["+", "-", "*", "/"].includes(value)) {
      operator = value;
      isNewNumber = true;
      firstNumber = display.textContent;
    }

    // 8. if '=': parse numbers, calculate result based on operator, update display, set isNewNumber to true
    else if (value === "=") {
      if (!operator || firstNumber === null) return; // safety check

      let temp = display.textContent;
      let operations = {
        "+": (a, b) => a + b,
        "-": (a, b) => a - b,
        "*": (a, b) => a * b,
        "/": (a, b) => {
          if (b !== 0) {
            return a / b;
          }
          // throw new Error("Error");
          return "Error";
        },
      };

      let result = operations[operator](
        parseFloat(firstNumber),
        parseFloat(temp),
      );

      // display.textContent = result;
      display.textContent =
        typeof result === "number" ? parseFloat(result.toFixed(10)) : result;

      firstNumber = null;
      operator = "";
      isNewNumber = true;
    }

    // 9. if '.': handle decimal (prevent multiple dots, handle starting fresh with '0.')
    else if (value === ".") {
      if (isNewNumber) {
        display.textContent = "0.";
        isNewNumber = false;
      } else if (!display.textContent.includes(value)) {
        display.textContent += value;
      }
    }

    // 10. if '+/-': toggle positive/negative sign
    else if (value === "+/-") {
      if (display.textContent > 0) {
        display.textContent = "-" + display.textContent;
      } else {
        display.textContent = String(-Number(display.textContent));
      }
    }

    // 11. if 'C': backspace / remove last digit
    else if (value === "C") {
      display.textContent = display.textContent.slice(0, -1);
      if (!display.textContent) {
        display.textContent = "0";
      }
    }
  });
});
