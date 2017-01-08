def greet(number,*dialog):    #一个*表示接受任何数量的实参
    #向列表中的每一个人发一句问候语
    for name in dialog:
        mes = "hello " + name.title() + "!"
        print(str(number) + " " + mes)
names = ['yan','yu','yi']
greet(1,'yu','yi','yan')
greet(2,'bin','yin')
def build_profile(first,last,**user_info):#两个**可以接受任意数量的关键字实参
    profile = {}
    profile['first name'] = first
    profile['last name'] = last
    for key,value in user_info.items():
        profile[key] = value
    return profile
user_profile = build_profile('albert','einstein',location='princeton',field='physics')
print(user_profile)


    
