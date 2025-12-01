# Q1. Set s_username = "Infosys", s_password = "123".
# Get input for username and password. Create a function called validate().
# If username and password match, the function should return True, else False.


s_username = "Infosys"
s_password = "123"

def validate(username, password):
    if username == s_username and password == s_password:
        return True
    else:
        return False

u = input("Enter username: ")
p = input("Enter password: ")

result = validate(u, p)
print("Login Successful:", result)



#######################################################################


# Q2. Compute (a + b) * c
# Get input for a, b, and c, and create a function called add() which should
#  return the sum of a and b, and multiply that sum with c.


def add(a, b):
    return a + b

a = int(input("Enter value for a: "))
b = int(input("Enter value for b: "))
c = int(input("Enter value for c: "))

sum_ab = add(a, b)
result = sum_ab * c

print(result)




