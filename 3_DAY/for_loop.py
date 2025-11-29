# for i in "apple":
# print(i)


# for i in range(1,5):
#     print(i)

# for i in range(11):
#     print(i)


# for i in range(1,11):
#     print(i, "x2=", i*2)



# Q1. get input for numbers a and b
# print the numbers between a and b

# a = int(input("Enter a value: "))
# b = int(input("Enter b value: "))

# for i in range(a,b):
#     print(i)


# Q2. print even nos between 1 to 10

# for i in range(1,11):
#     if i % 2 == 0:
#         print(i)


# Q3. count the odd nos between 1 to 10 

# count = 0

# for i in range(1,11):
#     if i % 2 != 0:
#         count = count + 1
# print(count)


# Q4. count the no which are divi by 3 and 5 range(1 to 100)

count = 0

for i in range(1,100):
    if i%3 == 0 and i%5 == 0:
        count += 1
print(count)

# Q5. write a program to compute the sum of first 
# 5 natural numbers

sum = 0

for i in range(1,6):
    sum = sum + i

print("sum of first 5 natural numbers: ", sum)



# Q6. write a program to read 10 numbers from the keyboard
# and find their sum and average

# total = 0

# print("Enter 10 numbers:")

# for i in range(10):
#     num = int(input())
#     total += num

# avg = total/10

# print("Sum of 10 numbers:", total)
# print("Average of 10 numbers:", avg)




###############################

for i in range(1,3):
    print("Week:",i)
    for j in range(1,4):
        print("Day:",j)


for i in range(1, 5):     
    for j in range(1, i+1):   
        print(j, end=" ")
    print()