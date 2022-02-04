from abc import abstractmethod


class car():
    pass


toyota = car()
honda = car()

toyota.modelname = "camry"
toyota.yearofmanufacture = "2019"
toyota.price = 4000

honda.modelname = "bold"
honda.yearofmanufacture = "2017"
honda.price = 3500
print(toyota.price)


##CONSTRUCTOR
class car():
    def __init__(self, modelname, yearofmanufacture, price):
        self.modelname = modelname
        self.yearofmanufacture = yearofmanufacture
        self.price = price

    def price_inc(self):
        self.price = int(self.price * 1.15)


toyota = car("camry", 2019, 5000)
honda = car("bold", 2017, 4500)
print(honda.__dict__)
print(honda.price)
honda.price_inc()
print(honda.price)


class Supercar(car):
    pass


honda = car("bold", 2017, 4500)
toyota = car("camry", 2019, 5000)

honda.cc = 1500
print(help(honda))
# print(honda.yearofmanufacture_)




