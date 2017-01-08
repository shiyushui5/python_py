class Car():
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
        self.road = 0                  #给属性默认值，不需要外部赋值

    def get_describe(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()
    def road_meter(self):
        print("This car has " + str(self.road) +" miles on it!")
    def update(self,mile):
        self.road += mile

class Battery():                        #建立一个新类，作为Elec_car的一个属性
    def __init__(self,battery_size = 251):
        self.battery_size = battery_size
    def describe_battery(self):
        print("This car has a " + str(self.battery_size) + "-kwh battery.")
    def year_car(self,yearcar):
        print("The car has " + str(yearcar) + " year old")
    def get_range(self):
        if self.battery_size == 251:
            range = 140
        elif self.battery_size == 120:
            range = 70
        mes = "The car can go " + str(range)
        mes += " mile on a full charge"
        print(mes)

#子类包含父类的所有的实例，父类不包含所有的子类实例
class Elec_car(Car):                      #子类必须在括号中包含父类，且在前面
    #电动汽车的特别地方        
    def __init__(self,make,model,year):  #接受创建Car所需要的信息
        super().__init__(make,model,year)#将子类与父类联系在一起
        self.battery = Battery()         #新的Battery实例存储在self.battery中
    def get_describe(self):
        long_name = "yan to " + str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name
        
new_car = Car('audi','a4',2013)
print(new_car.get_describe())
new_car.road_meter()
new_car.road = 250                       #new_car找到属性road，并重新赋值
new_car.road_meter()
new_car.update(52)
new_car.road_meter()
onecar = Elec_car('benchi','big',2014)
print(onecar.get_describe())
onecar.battery.describe_battery()
onecar.battery.year_car(5)
onecar.battery.get_range()