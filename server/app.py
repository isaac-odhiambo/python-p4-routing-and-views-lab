#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:hello>')
def print_string(hello):
    print(hello)  # Print to console
    return hello  # Return the parameter

@app.route('/count/<int:n>')
def count(n):
    # Ensure that the output matches the expected format with a trailing newline
    numbers = '\n'.join(str(i) for i in range(n)) + '\n'
    return numbers  # Return as plain text

@app.route('/math/<int:num1>/<string:operation>/<int:num2>')
def math(num1, operation, num2):
    """Perform basic math operations: +, -, *, div, %."""
    
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div':  # We use 'div' to avoid URL conflict with '/'
        result = num1 / num2
    elif operation == '%':
        result = num1 % num2
    else:
        return "Invalid operation", 400  # Return a 400 error for invalid operations
    
    # Returning the result as plain text
    return str(result)

if __name__ == '__main__':
    app.run(port=5555, debug=True)
