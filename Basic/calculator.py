# This code defines a simple calculator that can perform addition, subtraction, multiplication, and division.

def addition(a,b):
    c=a+b
    return c
def subtraction(a,b):
    c=a-b
    return c    
def multiplication(a,b):
    c=a*b
    return c
def division(a,b):
    if b==0:
        return "Error! Division by zero."
    else:
        c=a/b
        return c
def calculator():
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    choice=int(input("Enter choice (1/2/3/4): "))
    if choice in [1,2,3,4]:
        num1=float(input("Enter first number: "))
        num2=float(input("Enter second number: "))

    if choice==1:
        c=addition(num1,num2)
        print(f"The result is: {c}")
    elif choice==2:
        c=subtraction(num1,num2)
        print(f"The result is: {c}")
    elif choice==3:
        c=multiplication(num1,num2)
        print(f"The result is: {c}")
    elif choice==4:
        c=division(num1,num2)
        print(f"The result is: {c}")
    else:
        print("Invalid input")


calculator()
