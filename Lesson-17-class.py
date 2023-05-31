carname = input('Car name : ')
wheel = input('Car"s wheel : ')
class Car :
    def __init__(self,carname,wheel) :
        self.carname = carname
        self.wheel = wheel

    def drive(self) :
        print(f'{self.carname} is driving and it have {self.wheel} wheels.')

# car=Car('Lambo',4)
# car.drive()

car = Car(carname,wheel)
car.drive()