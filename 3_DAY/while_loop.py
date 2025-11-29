# count = 1
# while count <= 5:
#     print(count)
#     count += 1


#############################

# while True:
#     stuff = input("String to capitalize [type q to quit]:")
#     if stuff == "q":
#         break
#     print(stuff.capitalize())


###################

# while True:
#     value = input("Integer, please [q to exit]:")
#     if value == "q":
#         break
#     number = int(value)
#     if number%2 == 0:
#         continue
#     print(number, "squared is: ", number*number)



###################

# numbers = [1,3,5,4]
# position = 0
# while position < len(numbers):
#     number = numbers[position]
#     if number%2 == 0:
#         print("Found Even numbers", number)
#         break
#     position += 1

# else:
#     print("No Even number found")



################################

# Q1. write a loop statement to print the following series
# 10,20,30,40,50,60,.....200

i = 10
while i <= 200:
    print(i, end=" ")
    i += 10

# Q2. write a program to print first 10 natural nos

i = 10
while i >= 1:
    print(i)
    i -= 1


# Q3. write a prog to find factorial of given no

num = int(input("Enter a number: "))

factorial = 1
i = 1

while i <= num:
    factorial *= i
    i += 1

print("Factorial of", num, "is", factorial)






