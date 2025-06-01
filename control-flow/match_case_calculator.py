num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

operation = input("Choose the operation (+, -, *, /): ")

if operation == "+":
    result = (num1 + num2)
    print(f"The result is {result}")

elif operation == "-":
    result = (num1 - num2)
    print(f"The result is {result}")

elif operation == "*":
    result = (num1 * num2)
    print(f"The result is {result}")

elif operation == "/":
    while num2 > 0:
        result = (num1 / num2)
        print(f"The result is {result}")
        break
    else: print("The divisor can not be 0")


