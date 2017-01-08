from y01083f import Answer_survey
question = "what language did you first to learn?"
my_survey = Answer_survey(question)
my_survey.show_question()  #显示问题并存储答案
print("Enter 'a' at any time to quit.\t")
while True:
    response = input("language: ")
    if response == 'a':
        break
    my_survey.store_response(response)
print("\tThank you to everyone who participated in the survey!")
my_survey.show_result()
