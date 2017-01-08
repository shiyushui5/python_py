#import json
#username = input("what is your name?")

#filename = 'y01081f.json'
#with open(filename,'w') as f_name:
#    json.dump(username,f_name)
#    print("We'll remember you when you come back, " + username + "!")
import json

def get_stored():
    #如果存储了用户名，就获取它
    filename = 'y01081f.json'
    try:
        with open(filename) as f_name:
            username = json.load(f_name)
    except FileNotFoundError:
        return none
    else:
        return username
def greet_user():
    #问候用户，并指出其名字
    username = get_stored()
    if username:
        print("Welcome back, " + username + "!")
    else:
        username = input("what is you name?")
        filename = 'y01081.json'
        with open(filename,'w') as f_name:
            json.dump(username,f_name)
            print("We'll remember you when you come back," + username + "!")
#先获取文件中的用户名，再根据是否存在用户名，来打招呼还是重新创建用户名
greet_user()

