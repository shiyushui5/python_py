import unittest
from y01082f import get_fullname
class NamesTestCase(unittest.TestCase):          #创建一个自己命名的类，继续继承unittset.TestCase的类
    #测试y01082f.py
    def test_firtlast_name(self):
        full_name = get_fullname('janis','joplin')
        self.assertEqual(full_name,'Janis Joplin')
unittest.main()