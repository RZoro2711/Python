class Car :
    sterringwheel = 1
    def __init__(self,carname,wheel) :
        self.carname = carname
        self.wheel = wheel

    def drive(self) :
        print(f'{self.carname} is driving and it have {self.wheel} wheels.')

    @classmethod
    def method(cls) : 
        print(f'All car has {cls.sterringwheel} sterring wheel.')


# car=Car('Lambo',4)
# car.drive()
# Car.method()
# car.method()
# print(car.sterringwheel)