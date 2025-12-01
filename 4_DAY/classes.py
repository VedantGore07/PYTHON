class Vehicle:
    def __init__(self,make,model):
        self.make = make
        self.model = model

    def moves(self):
        print("moves along...")

    def get_make_model(self):
        print(f"This car manufactured by {self.make} model name{self.model}")


my_car = Vehicle('Tesla','ModelY')
my_car.moves()
my_car.get_make_model()
print(my_car.make)
print(my_car.model)

your_car = Vehicle('Tata','Nexon')
your_car.moves()
your_car.get_make_model()
print(your_car.make)
print(your_car.model)



print("\n\n")


######################################

# inheritance

class Airplane(Vehicle):
    def moves(self):
        print("moves along...")


class Truck(Vehicle):
    def moves(self):
        print('Rumbles along...')


class GolfCart(Vehicle):
    pass

cessna = Airplane('cessna','Skyhawk')
mack = Truck('Mack', 'Pinnacle')
golfwagon = GolfCart('Yamaha','RX100')

cessna.get_make_model()
cessna.moves()

mack.get_make_model()
mack.moves()

golfwagon.get_make_model()
golfwagon.moves()


