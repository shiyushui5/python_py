yy = ['chen','yu','yan']
print (str(yy) + " 一起赴约!",end = "")
del yy[0]
print (yy[0] + ' 不能赴约',end = "")
yy.append('sun')
print (yy[2] + " 新增赴约的一人",end = "")
yy.insert(2,'you')
print (yy[2] + " 又增一人！",end = "")
yy_pop = yy.pop(2)
print (yy_pop + " 突然有事不能来！",end = "")
print (str(yy) + " 目前确定的人数",end = "")
yy.remove('yu')
print (str(yy) + " 最终确定的人数",end = "")