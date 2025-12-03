# w+ --> if file already exists?

f1 = open("file_1.txt","w+")
print(f1.tell())
f1.write("Hi welcome")
f1.write("This is Python Session for PDA Batch")
f1.seek(0)
print(f1.read())
f1.close()











