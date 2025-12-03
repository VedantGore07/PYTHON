# rb --> read binary file
f1 = open("yorichi.jpg","rb")
print(f1.read())


f1 = open("yorichi.jpg","rb")
f2 = open("yorichi2.jpg","wb")
for i in f1:
    f2.write(i)



