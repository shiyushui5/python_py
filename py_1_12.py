yy0 = {'color':'blue','size':'big'}
yy1 = {'color':'red','size':'small'}
yy2 = {'color':'green','size':'medium'}
yy = [yy0,yy1,yy2]
#for yy_0 in yy:
#    print (yy_0)
yy = []
#yy_num这是用来循环的，代表循环的次数
for yy_num in range(26,30):
   yy4 = {'color':'yellow','size':'too'}
   yy.append(str(yy4) + str(yy_num))
for yy_x in yy[0:29]:
    print (yy_x)
print ("Total number of yy:" + str(len(yy)))
yy = {'color':['red','blue'],'chara':['hi','yu']}
print (yy)
print (yy['color'][1])
users = {
        'aeinstein':{
                     'first':'albert',
                     'last':'einstein',
                     'location':'princeyon',},
        'mcurie':{
            'first':'marie',
            'last':'curie',
            'location':'paris',},}
for username,user_info in users.items():
    print("\nUsername: " + username)
    full_name = user_info['first'] + " " + user_info['last']
    location = user_info['location']
    print ("\tfull name: " + full_name.title())
    print("\tlocation: " + location.title())
    
