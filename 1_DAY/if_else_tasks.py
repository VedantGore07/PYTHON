#get input variable income

income = int(input("Enter your income: "))
if(income < 70000):
    print("Scolarship is availble")
else:
    print("Scolarship not availble")

#task3
#id divisble by 3 & 5 both

num = int(input("Enter the number: "))
if(num%3 == 0 and num% 5 == 0):
    print("Divisble by 3 and 5 both")
else:
    print("Not Divisble by 3 and 5")

#task4
#even or odd
num1 = int(input("Enter the number: "))
if(num1 % 2 == 0):
    print("EVEN")
else:
    print("ODD")


#task5:
a = int(input("Enter the score of student: "))
if(a < 35):
    print("Poor student")
elif(a > 35 and a < 70):
    print("Average student")
elif(a > 70 and a <= 100):
    print("Good student")
else:
    print("Invalid score")

#task6
#nested if
#
sal = int(input("Enter the salary: "))
age = int(input("Enter the age: "))
if(sal > 20000 or age <= 25):
    reqLoan = int (input("Enter the required amount of loan"))
    if(reqLoan <= 50000):
        print("Eligible for loan: ")
    else:
        print("Maximum loan amount is 50000")


#task7
#mini calculator
a1 = int(input("Enter first number: "))
b = int(input("Enter second number: "))
operation = input("Enter operation to be performed (add/sub/mul/div)")

if operation == "add":
    print("Result:", a1 + b)

elif operation == "sub":
    print("Result:", a1 - b)

elif operation == "mul":
    print("Result:", a1 * b)

elif operation == "div":
    if b == 0:
        print("Cannot divide by zero!")
    else:
        print("Result:", a1 / b)

else:
    print("Invalid operation selected")

#task8
percentage = float(input("Enter your score percentage: "))

if percentage > 70:
    name = input("Enter your name: ")
    department = input("Enter your department: ")
    location = input("Enter your location: ")

    print("You are eligible!")
else:
    print("You are not eligible.")

