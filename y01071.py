from y01062 import Car   #只是导入Car类和其他的主程序，所以会运行
mynew_car = Car('dongfeng','ar',2014)
print(mynew_car.get_describe())
#mynew_car1 = Elec_car('yiqi','ae',2078)    #Elec_car这个类并没有被导入
#print(mynew_car1.get_describe())
from y01062 import Car,Elec_car    #导入多个类
from y01062 import *              #导入文件中的所有的类