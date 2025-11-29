myTuple = ('Pushkar', 42, True)
anotherTuple = (1, 2, 8, 4, 9, 5)

print(myTuple)
print(anotherTuple)

print(type(myTuple))
print(type(anotherTuple))

newlist = list(anotherTuple)   

newtuple = tuple(newlist)
print(newtuple)
print(type(newtuple))

print("unpacking tuple items")

(one, *two, three) = anotherTuple
print(one)
print(two)
print(three)

print(anotherTuple.count(2))