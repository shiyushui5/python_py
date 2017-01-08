class Dog():
    def __init__(self,name,age):#左右两边的下划线都是两个，一共就是四个
        #初始化属性name和age
        self.name = name        #将自动传递实参self指向实例本身作用,类似全局变量
        self.age = age

    def sit(self):
        #模拟小狗被命令时蹲下
        print(self.name.title() + " is now sitting.")
        
    def roll_over(self):
        #模拟小狗被命令时打滚
        print(self.name.title() + " rolled over!")
my_dog = Dog('blue',250)        #my_dog返回Dog（）中实例,后面加.sit（）就能调用
my_dog.sit()
print("My dog's name is " + my_dog.name.title() + ".")
print ("My dog is " + str(my_dog.age) + " years old.")
you_dog = Dog('red',520)    #可根据类创建多个实例
print("You dog's name is " + you_dog.name.title() + ".")
print ("You dog is " + str(you_dog.age) + " years old.")
