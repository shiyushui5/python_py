#默认将yy为字符型！
#yy = input("tell me something,and i will repeat it: ")
#print ("hello " + str(yy) + "!")
prompt = "if you tell us who you are,we can personalize the messages you see."
prompt += "\nwhat is you first name? "
#yy1 = input(prompt)
prompt = "\nwahat is you last name?"
#yy = input(prompt)
#print ("Hello," + yy + yy1 + "!")
#age = input ("how old are you? ")
yy = input ("how old are you? ")
age = int(yy)
if age%2 == 0:
    print ("the age " + str(age) + " is odd")
else:
    print ("the age " + str(age) + " is even")
