yy = 5
while yy <= 7:
    print(yy,end = "")
    yy = yy + 1
prompt = "\ntell me something,and i will repeat it back to you: "
prompt += "\nenter 'quit' to end the program."
active = True
while active:
    yy = input(prompt)
    if yy == 'quit':
        break
#        active = False
    else:
        print(yy)
#while yy != 'quit':
#    yy = input(prompt)
#    if yy != 'quit':
#        print(yy,end = "")

