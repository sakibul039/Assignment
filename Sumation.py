# Sumation
print("select an operation to perform")
print("1. ADDITION")
print("2. SUBTRACT")
print("3. MULTIPLY")
print("4. DIVIDE")
print("5. EXIT")

operation = input("Enter a Number: ")


if operation == "1":
    num1 = input("enter first number: ")
    num2 = input("enter second number: ")
    print("the sum is " + str(int(num1) + int(num2)))
elif operation == "2":
      num1 = input("enter first number: ")
      num2 = input("enter second number: ")
      print("the sum is " + str(int(num1) - int(num2)))
elif operation == "3":
      num1 = input("enter first number: ")
      num2 = input("enter second number: ")
      print("the sum is " + str(int(num1) * int(num2)))
elif operation == "4":
      num1 = input("enter first number: ")
      num2 = input("enter second number: ")
      print("the sum is " + str(int(num1) / int(num2)))

else:
    print("Invalid Entry")
