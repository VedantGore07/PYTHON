# 3. Create a class called Animal() with a method sound() that prints "Animal makes a sound".
#  Create a derived class called Dog that inherits from Animal and overrides 
# the sound() method to print "Dog barks". Create another Derived class called
#  Bird that inherits from Animal and overrides the sound() method to print "Birds Sing"



class Animal():
    def sound(self):
        print("Animal makes a sound")

a1 = Animal()
a1.sound()


class Cat(Animal):
    pass


class Dog(Animal):
    def sound(self):
        print("Dog barks")

d1 = Dog()
d1.sound()

c1 = Cat()
c1.sound()


class Bird(Animal):
    def sound(self):
        print("Bird sings")


b1 = Bird()
b1.sound()



















