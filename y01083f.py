class Answer_survey():           #创建一个类的首字母必须大写
    def __init__(self,question):
        #存储一个问题
        self.question = question
        self.responses = []         #在类中创建全局列表

    def show_question(self):
        #显示调查问卷
        print(self.question,end = "")

    def store_response(self,new_response):
        #存储单份调查问卷
        self.responses.append(new_response)

    def show_result(self):
        print("survey results: ")
        for response in self.responses:
            print('-' + response,end = "")
            