def hello_world():
    print("Hello World")

hello_world()

##########################

# def sum(num1,num2):
#     return num1+num2

# print(sum(10,20))


##########################

def do_nothing():
    pass

print("do nothing function")
do_nothing()


##########################

def sum(num1,num2):
    if(type(num1) is not int or type(num2) is not int):
        return
    return num1+num2

print(sum(10.5,20))


##########################

def multiple_items(*args):
    print(args)
    print(type(args))

multiple_items("Devi","Gayathri")


##########################

def add(*num):
    sum = 0
    for n in num:
        sum = sum + n
    print("Sum:",sum)

add(10,20,30,40)


##########################

def multi_named_items(**kwargs):                 #kwargs - key word args
    print(kwargs)
    print(type(kwargs))

multi_named_items(first_name="Virat", last_name="Kohli", location="Bengaluru")


##########################

# def func(a,b,*args,option=False,**kwargs):
#     print(' ')
#     print(a,b)
#     print(args)
#     print(option)
#     print(kwargs)


# func(1,3,10,20,Name="Virat",salary=92000)

##########################

# print("usage of default values")
# def func1(a,b=4):
#     print(' ')
#     print(a,b)

# func1(1,7)


##########################

# def add_one(num):
#     if(num>=9):
#         return num+1
#     total = num+1
#     print(total)
#     return add_one(total)

# mynewtotal = add_one(0)
# print(mynewtotal)


##########################

# Q1. prog to print factorial of anumber recursively

# recursive function

def recursive_factorial(n):
    if n==1:
        return n
    else:
        return n*recursive_factorial(n-1)
    
# user input
num = 6

if num<0:
    print("Invalid input! please enter a positive number")
elif num == 0:
    print("factorial of number 0 is 1")
else:
    print("factorial of number", num, "-", recursive_factorial(num))




##########################

# Function exercise

# Q1.Create a function called add(), sub(), mul(), div() and 
# get the input for a and b inside every function then print the result.

def add():
    a = float(input("Enter value for a: "))
    b = float(input("Enter value for b: "))
    print("Addition =", a + b)

def sub():
    a = float(input("Enter value for a: "))
    b = float(input("Enter value for b: "))
    print("Subtraction =", a - b)

def mul():
    a = float(input("Enter value for a: "))
    b = float(input("Enter value for b: "))
    print("Multiplication =", a * b)

def div():
    a = float(input("Enter value for a: "))
    b = float(input("Enter value for b: "))
    if b == 0:
        print("Cannot divide by zero")
    else:
        print("Division =", a / b)


add()
sub()
mul()
div()



##########################

# Q2.Get an integer number from user and pass it to the 
# function called findeveorodd(). Let the function print whether number is even or odd.

def findeveorodd(num):
    if num % 2 == 0:
        print(num, "is Even")
    else:
        print(num, "is Odd")


n = int(input("Enter an integer: "))
findeveorodd(n)


##########################

# Q3. Get input for a and b and pass it to the function 
# called printrange(). Let the function print numbers from a to b.

def printrange(a, b):
    for i in range(a, b + 1):
        print(i, end=" ")
    print()


a = int(input("Enter a: "))
b = int(input("Enter b: "))
printrange(a, b)






























