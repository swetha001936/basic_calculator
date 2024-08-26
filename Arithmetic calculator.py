import math


print("-------Arithmetic calculator-------")
while True:
   
    print("1. Addition operation")
    print("2. Subtraction operation ")
    print("3. Multiplication operation")
    print("4. Division opeartion")
    print("5. Square Root operation")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == '6':
        print("Exiting the calculator. you can continue...!")
        break

    if choice not in ['1', '2', '3', '4', '5', ]:
        print("Invalid choice. Please enter a number between 1 and 6.")
        continue

    if choice in ['1', '2', '3', '4', '5']:
        number_1= int(input("Enter the first number: "))
        number_2= int(input("Enter the second number: "))

    if choice == '1':
        result = number_1 +number_2
        operation = "Addition"
    elif choice == '2':
        result =number_1 - number_2
        operation = "Subtraction"
    elif choice == '3':
        result = number_1 * number_2
        operation = "Multiplication"
    elif choice == '4':
        if number_2 != 0:
            result = number_1 / number_2
            operation = "Division"
        else:
            print("Error--you can't Divide  by zero.")
            continue
    elif choice == '5':
        if number_1 >= 0:
            result = math.sqrt(number_1)
            operation = "Square Root"
        else:
            print("Error--you Cannot calculate square root of this  number.")
            continue

    print("{operation} Result: {result}\n")