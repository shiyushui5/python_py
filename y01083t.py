import unittest
from y01083f import Answer_survey

class Test_three_survey(unittest.TestCase): #包含测试类
    #针对Answer_survey类的测试
    def setUp(self):                          #python先运行setUp，然后才运行所有test_的方法
        question = "what language did you first learn to speak?"
        self.my_survey = Answer_survey(question)      #创建了一个所有方法都能使用的实例
        self.responses = ['china','english','yan']    #创建了所有方法都能使用的变量
    def test_one_store(self):
        #question = "what language did you first learn to speak?"
        #my_survey = Answer_survey(question)
        #my_survey.store_response('English')
        self.my_survey.store_response(self.responses[0])
        self.assertIn(self.responses[0],self.my_survey.responses)#此时相当于self.responses，即存储全类变量
    def test_three_store(self):
        #question = "what language did you first learn to speak?"
        #my_survey = Answer_survey(question)
        #responses = ['china','english','yan']
        for response in self.responses:
            self.my_survey.store_response(response)         #将responses每一个都传回到类中
        
        for response in self.my_survey.responses:
            self.assertIn(response,self.responses)#检查类中列表和responsrs是否一致
unittest.main()