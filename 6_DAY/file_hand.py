# r+ --> file is exists already

f1 = open("file_1.txt","r+")
print(f1.tell())
print(f1.read())
print(f1.tell())
f1.write("Practice makes perfect")
print(f1.tell())
print(f1.read())
print(f1.tell())












