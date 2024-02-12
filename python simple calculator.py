while True :
    num1 = float(input ("Enter the first number :  "))
    num2 = float (input("Enter the second number :  "))
    operation = str(input ("Enter the operation ( + , - , * , /  )  : "))

    if  operation  == "+" :
        result = num1 + num2
    elif operation == "-" :
        result = num1 - num2
    elif operation == "*" :
        result = num1 * num2
    elif operation == "/" :
        if num2 == 0 :
            print( " Error , division by zero ")
        else :
            result == num1 / num2
            break
    else :
        print( "Invalid operation. This calculator supports only +, -, *, and /.")
                        
    print ( result )
