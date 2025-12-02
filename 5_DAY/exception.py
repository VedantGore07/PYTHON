# print("Hi")
# print("hello")
# printt("hey")        # nameerror


# print(x)             # nameerror

# a = int(input())
# b = int(input())
# print(a+b)             # ValueError: invalid literal for int() with base 10: 'hi'



#####################################################

# try:
#     a = int(input("Enter a value:"))
#     b = int(input("Enter b value"))
#     print(a+b)
# except Exception as e:
#     print("Something went wrong",e)



# try:
#     a = input("Enter first string:")
#     b = input("Enter second string:")
#     print(a/b)
# except Exception as e:
#     print("something",e)




# try:
#     a = int(input())
# except ValueError as e:
#     print("valueError",e)




# try:
#     a = int(input())
#     b = int(input())
#     c = input()
#     print(c/a)
#     print(d)
# except ValueError as e:
#     print("Value Error",e)
# except TypeError as e:
#     print("type Error",e)
# except Exception as e:
#     print("something wrong",e)
# finally:
#     print("Done")




# try:
#     print(x)
# except NameError:
#     print("Name Error means something is not probably defined")




x = 12
try:
    print(x/0)
except ZeroDivisionError as e:
    print("please dont divide by zero",e)
except Exception as e:
    print("Something wrong",e)
else:
    print("No Error!")
finally:
    print("I am going to print with error or without error")




























