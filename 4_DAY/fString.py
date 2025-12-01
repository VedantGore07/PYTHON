person = "Anuksha"
Goldmedal = 3

print("\n" +person+ " has " + str(Goldmedal) + " Gold medals")

message = "\n %s has %s Gold medals" %(person,Goldmedal)
print(message)


# string.format() method
message = "\n {} has {} Gold medals".format(person,Goldmedal)
print(message)


message = "\n {1} has {0} Gold medals".format(Goldmedal,person)
print(message)


message = "\n {person} has {Goldmedal}".format(Goldmedal=Goldmedal, person = person)
print(message)


player = {'person':'Anuksha',
          'Goldmedal':3}

message = "\n{person} has {Goldmedal} Goldmedal".format(**player)
print(message)



# fstring
message = f"\n {person} has {Goldmedal} Goldmedals"
print(message)


message = f"\n {person} has {2*5} Goldmedals"
print(message)

message = f"\n {player['person']} has {2*5} Goldmedals"
print(message)


num = 10
print(f"\n 2.25 times {num}, {2.25*num:.2f}")
