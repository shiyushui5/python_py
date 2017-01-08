#前提条件是 函数（以.py格式存取）和主程序在同一个文件下
import y01053    #定义函数的文件名
y01053.make_pizza(13,'pepperoni')  #定义函数的文件名加上函数名
y01053.make_pizza(250,'mushrooms','green pepers','extra cheese')
y01053.make_bing('blue','sugar','tasty','delicious')
from y01053 import make_pizza
make_pizza(250,'mushrooms','green pepers','extra cheese')
from y01053 import make_bing
make_bing('red','cool','distasty','undelicious')
import y01053 as p      #将make_pizza取别名，以别名取代函数前面的文件名
p.make_pizza(15,'bad')
from y01053 import *    #导入文件中的所有函数
make_pizza(325,'sugar and good')