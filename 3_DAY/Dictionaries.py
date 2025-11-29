#{}

car = {
    "brand":"Tesla",
    "model":"model_3_p",
    "year":2024
}

car2 = dict(brand="Tesla", model="model_3_p")

print(car)
print(car2)


print(car.get("model"))

# list all keys

print(car.keys())
print(car.values())

# list of key/value pairs as tuples
print('')
print(car.items())


# verify a key exists
print("model" in car)    #True
print("price" in car)    #False


# change values
car["brand"]="Nio"
car["EV"]="No"
car.update({"price":1000000})
print('')

print("updated car values")
print(car)


'''
# remove items
print(car.pop("price"))
print('')
print(car)


# delete items
del car["model"]
print(car)


# clear -- deleting everything
print("clear")
car.clear()
print(car)

'''


# copy of dict

car3 = car    #create a reference
print('')
print("Bad copy")
print(car)
print(car3)

# first way  - copy function
car4 = car.copy()
print("Good copy")
print(car4)
print(type(car4))


# second way  - copy function
# use dict()

car5 = dict(car)
print("copy of car in car5")
print(car5)


# Nested Dictonaries
member1 = {
    "name":"Bharathi",
    "id":369
}

member2 = {
    "name":"Ravi",
    "id":785
}

Group = {
    "member1" : member1,
    "member2" : member2
}

print('')
print(Group)

print(Group["member1"])

print(Group["member2"]["name"])







