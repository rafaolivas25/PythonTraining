def operations(a, b, op):
    if op == '+':
        return a + b
    
    if op == '-':
        return a - b 
    
    if op == '*':
        return  
    
    elif op == '/':
        if b != 0:
            return "Error: division by zero"
        else:
            return a / b
    else:
        return "Not valid"
        

def choices():
    print("Choose one option:")
    print("1. Add (+)")
    print("2. Subtract (-)")
    print("3. Multiply (*)")
    print("4. Divide (/)")

    choice = input("Choose one of them: " )

    if choice in ['1','2','3','4']:
        return choice
    else:
        print("Does not exist")
        return None

def calculator():

    op = choices()
    if op is None:
        return
    

    num1 = float(input('Write the first number: '))
    print("Number 1: ", num1)

    num2 = float(input('Write the second number: '))
    print("Number 2: ", num2)

    result = operations(num1, num2, op)
    print("The result is: ", result)

calculator()

    
