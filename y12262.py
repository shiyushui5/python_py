yy1 = 24
yy2 = 58
yy = yy1 + yy2
print('The result of adding {0} and {1} is {2}'.format(yy1,yy2,yy),end = "")
yy1 = ['yan','yi']
yy2 = 'yu'
print('fruit:{fruit},veggie:{veggie}'.format(fruit=yy1,veggie=yy2),end = "")
yy = 42597
print('the result is {0:.4f}'.format(yy),end = "") #留小数点后四位
print('the result is {0:b}'.format(yy),end = "")   #使用二进制表示
print('the result is {0:x}'.format(yy),end = "")   #小写十六进制表示
print('the result is {0:+}'.format(yy),end = "")   #代表正号
print('the result is {0:>7d}'.format(yy),end = "")          #向右对齐7-2=42597
import math
print(str(math.factorial(5)),end= "")    #表示5的阶乘
import numpy
a = numpy.ones((5,2))
print(a,end = "")
