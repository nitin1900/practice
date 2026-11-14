const display = document.querySelector('.display');
const buttons = document.querySelectorAll('button');
let firstNumber = '';
let operator = '';
let isNewNumber = false; // Tells the calculator if the next digit should start fresh


buttons.forEach(button => {
    button.addEventListener('click', () => {
        const value = button.innerText;
        // 1. If AC is clicked, reset screen to 0
        if (value === 'AC') {
            display.innerText = '0';
            firstNumber = '';
            operator = '';
            isNewNumber = false;
        }
        // 2. If a number (0-9) is clicked
        else if ('0123456789'.includes(value)) {
            if (display.innerText === '0' || isNewNumber) {
                display.innerText = value;// Replace the initial 0
                isNewNumber = false;
            } else {
                display.innerText += value;// Append the number
            }
        }
        // 3. If an operator (+, -, *, /) is clicked
        else if (['+', '-', '*', '/'].includes(value)) {
            firstNumber = display.innerText;
            operator = value;
            isNewNumber = true;
        }
        // 4. If = is clicked, calculate!
        else if (value === '=') {
            const num1 = parseFloat(firstNumber);
            const num2 = parseFloat(display.innerText);
            let result = 0;

            if (operator === '+') result = num1 + num2;
            if (operator === '-') result = num1 - num2;
            if (operator === '*') result = num1 * num2;
            if (operator === '/') result = num1 / num2;

            display.innerText = result;
            isNewNumber = true; // Next number will start fresh
        }
        // 5. If decimal point is clicked
        else if (value === '.') {
            // If we are starting a new number, start with "0."
            if (isNewNumber) {
                display.innerText = '0.';
                isNewNumber = false;
            }
            // Otherwise, only add a dot if there isn't one already!
            else if (!display.innerText.includes('.')) {
                display.innerText += '.';
            }
        }
        // 6. If +/- is clicked
        else if (value === '+/-') {
            display.innerText = (parseFloat(display.innerText) * -1).toString();
        }
        // 7. If C (backspace) is clicked
        else if (value === 'C') {
            if (display.innerText.length > 1) {
                display.innerText = display.innerText.slice(0, -1);
            } else {
                display.innerText = '0';
            }
        }
    });
});