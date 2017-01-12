yy = '''this is
a so 
stuipd pig!'''
yy1 = 'this a smart \
dogs.'
print(yy + "\t" + yy1,end = "")
print(yy[6] + " " + yy1[2] + " " + yy[2:8],end = "")  #真正的是2到7，8不算在其中
yy2 = yy1.split()                     #将字符串分割成列表
print(yy2,end = "")
yy2[3] = 'yan'
yy4 = ' '.join(yy2)                 #将列表连接成字符串
print(yy2,end = "")
yy_num = yy1.rfind('dogs')
print(yy_num,end = "")