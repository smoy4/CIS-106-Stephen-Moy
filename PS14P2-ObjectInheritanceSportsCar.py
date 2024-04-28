# Stephen Moy
# CIS 106 - W01
# 04/24/2024

# Problem Set 14 - Problems 2: Car/SportsCar Class/Object/Inheritance

class Car:
  def __init__(self, make, model, stickerprice):
    self.make = make
    self.model = model
    self.stickerprice = stickerprice
    self.discountprice = stickerprice * 0.9

class SportsCar(Car):
  def __init__(self, make, model, stickerprice):
    super().__init__(make, model, stickerprice)
  def sportswheels(Car):
    Car.stickerprice = Car.stickerprice + 1000
    return Car.stickerprice
  def sportsengine(Car):
    Car.stickerprice = Car.stickerprice + 3000
    return Car.sportsengine
  def sportsinterior(Car):
    Car.stickerprice = Car.stickerprice + 2000
    return Car.sportsengine
  def postmodpricediscount(Car):
    Car.postmodpricedisc = Car.stickerprice * 0.9
    return Car.postmodpricedisc

car1 = Car("Honda", "CR-V", 30000)
car2 = Car("Lexus", "RX-350", 50000)

sportscar1 = SportsCar("Lamborghini", "Huracan", 400000)    # no modifcations
sportscar2 = SportsCar("Lamborghini", "Huracan", 400000)    # all modifications
sportscar3 = SportsCar("Lamborghini", "Huracan", 400000)    # custom job, use prompts

print("Car 1 Make:\t\t\t " + car1.make)
print("Car 1 Model:\t\t " + car1.model)
print("Car 1 Sticker Price: $" + format(car1.stickerprice, ".2f"))
print("Car 1 Discount Price: $" + format(car1.discountprice, ".2f"))

print("\n\nCar 2 Make:\t\t\t " + car2.make)
print("Car 2 Model:\t\t " + car2.model)
print("Car 2 Sticker Price: $" + format(car2.stickerprice, ".2f"))
print("Car 2 Discount Price: $" + format(car2.discountprice, ".2f"))

print("\n\nSports Car 1 (NO Modifications):")
print("Sports Car 1 Make:\t\t " + sportscar1.make)
print("Sports Car 1 Model:\t\t " + sportscar1.model)
print("Sports Car 1 Sticker Price: $" + format(sportscar1.stickerprice, ".2f"))
sportscar1.postmodpricediscount()
print("Sports Car 1 Discount Price: $" + format(sportscar1.postmodpricedisc, ".2f"))

print("\n\nSports Car 2 (ALL Modifications):")
print("Sports Car 2 Make:\t\t " + sportscar1.make)
print("Sports Car 2 Model:\t\t " + sportscar1.model)
sportscar2.sportswheels()
sportscar2.sportsengine()
sportscar2.sportsinterior()
print("Sports Car 2 Sticker Price: $" + format(sportscar2.stickerprice, ".2f"))
sportscar2.postmodpricediscount()
print("Sports Car 2 Discount Price: $" + format(sportscar2.postmodpricedisc, ".2f"))

print("\n\nSports Car 3 (Custom Job):")
print("Sports Car 3 Make:\t\t " + sportscar3.make)
print("Sports Car 3 Model:\t\t " + sportscar3.model)
print("Sports Car 3 Sticker Price (before modifications): $" + 
      format(sportscar1.stickerprice, ".2f"))

r1 = input("\nDo you want to add sports wheels for $1000? (Y/N):")
if r1 == "Y" or r1 == "y":
  sportscar3.sportswheels()
r2 = input("Do you want to upgrade to a sports engine for $3000? (Y/N):")
if r2 == "Y" or r2 == "y": 
  sportscar3.sportsengine()
r3 = input("Do you want to add sports interior for $2000? (Y/N):")
if r3 == "Y" or r3 == "y":
  sportscar3.sportsinterior()

print("\nSticker Price (after modifications): $" + 
      format(sportscar3.stickerprice, ".2f"))
sportscar3.postmodpricediscount()
print("Sports Car 3 Discount Price:\t\t $" + format(sportscar3.postmodpricedisc, ".2f"))