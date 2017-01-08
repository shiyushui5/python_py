import unittest
from y01082f import get_fullname
class NamesTestCase(unittest.TestCase):          #创建一个自己命名的类，继续继承unittset.TestCase的类
    #测试y01082f.py
    def test_firtlast_name(self):              #方法的开头必须以test_开头
        full_name = get_fullname('janis','joplin')
        self.assertEqual(full_name,'Janis Joplin') #比较full_name与后面的值是否一致
             #调用unittest的方法assertEqual()进行比较输出
    def test_fullname(self):
        full_name = get_fullname('yu','yan','yi')
        self.assertEqual(full_name,'Yu Yi Yan')          
unittest.main()   #让python运行这个文件中的测试
#输出E   表示测试中有一个单元测试出现错误
 
#assertEqual(a,b)             a == b
#assertNotEqual(a,b)          a != b
#assertTrue(x)                x为True
#assertFalse(x)               x为False
#assertIn(item,list)          核实item在list中
#assertNotIn(item,list)       核实item不在list中