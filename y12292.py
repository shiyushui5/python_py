#yy = (200,50)
#print (yy[0],end = "")
#print (yy[1],end = "")
#for yy1 in yy:
#    print (yy1,end = "")
#print (yy,end = "")
#yy = (400,200)
#print (yy,end = "")
#yy1 = ['chen','you','yi','yu','yan']
#for yy1 in yy:
#    if yy1 == 'yan':
#        print (yy1.upper() + "  " + str((yy1 == 'yan')),end = "")
#        print (yy1 == 'yan',end = "")
#    if yy1 == 'you':
#        print (yy1.title(),end = "")
#    else:
#            print (yy1,end = "")
#print ("输入完毕！",end = "")
#yy1 = 'YAN 
#print (yy1.upper() != 'yan',end = "")
#yy1 = 27
#yy2 = 1
#yy3 = 15
#print (yy3 >= yy2 or yy3 >= yy1,end = "")
#yy1 = 'you'
#if yy1 in yy:
#    print ('yeah',end = "")
#print ('yes',end = "")
#else:
#print ('nono',end = "")
#print ('yuj' in yy,end = "")
#if yy < 5:
#    print ("不收取任何费用！",end = "")
#elif yy < 20:
#    print ("收取一半的费用！",end = "")
#elif yy < 60:
#    print ("收取全额！",end = "")
#else:
#    print ("免费！",end = "")
#if 'yan' in yy1:
#    print ('good',end = "")
#if 'hu' in yy1:
#    print ('bad',end = "")
#if 'bing' in yy1:
#    print ('yiban',end = "")
yy = ['red','green','biue','blank']
yy1 = ['yu','yan','red','blue','su','blank']
for yy11 in yy1:
    if yy11 in yy:
        print ("可以提供此颜色！",end = "")
    else:
        print ("由于此店没有这个颜色，故不能提供!",end = "")
print ("客人选择完毕！",end = "")
