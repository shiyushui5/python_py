class Restaurant():
    def __init__(self,name,type_s):     #以self为前缀变量都可供类中的所有方法（函数）使用
        self.name = name                    
        self.type_s = type_s
    def describe_rest(self):
        print("The name is " + self.name.title() + " with " + self.type_s.title())
    def open_rest(self):
        print("please call " + self.name.lower())
new_rest = Restaurant('yan','nice')
new_rest.describe_rest()
new_rest.open_rest()
