def print_operation(num1, num2, operation):
    # Validate operation
    if operation not in ['+', '-', '*', '/']:
        raise ValueError("Unsupported operation. Use '+', '-', '*', or '/'.")
    
    # Validate that inputs can be converted to integers
    try:
        num1_int = int(num1)
        num2_int = int(num2)
    except ValueError:
        raise ValueError("Input strings must be convertible to integers.")
    
    # Handle division by zero
    if operation == '/' and num2_int == 0:
        raise ZeroDivisionError("Division by zero is not allowed.")
    
    # Perform the operation
    if operation == '+':
        result = num1_int + num2_int
    elif operation == '-':
        result = num1_int - num2_int
    elif operation == '*':
        result = num1_int * num2_int
    elif operation == '/':
        result = num1_int / num2_int
    
    return f"{num1} {operation} {num2} = {result}"

