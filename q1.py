def print_operation(num1, num2, operation):
    # TODO: Your code is here
    islem = ["+","-","*","/"]
    if operation not in islem:
        raise ValueError("Unsupported operation. Use '+', '-', '*', or '/'.")
        
    
    
    try:
        num11 = int(num1)
        num22 = int(num2)
    
    except ValueError:
        print("Input strings must be convertible to integers.")
    
    
    
    if operation == '/' and num22 == 0:
        raise ZeroDivisionError("Division by zero is not allowed.")
        
        
        
    
    
    if operation == '+':
        result = num11 + num22
    elif operation == '-':
        result = num11 - num22
    elif operation == '*':
        result = num11 * num22
    elif operation == '/':
        result = num11 / num22
    
    

    return f"{num1} {operation} {num2} = {result}"
