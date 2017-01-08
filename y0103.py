unyy = ['blue','yowllo','red','green']
yy = []
while unyy:
    yy1 = unyy.pop()
    print ("verifying user: " + yy1.upper(),end = "")
    yy.append(yy1)
print ("\tThe following users has been confiemed: ",end = "")
for yy2 in yy:
    print (yy2 + "  ",end = "")
while 'red' in yy:
    yy.remove('red')
print ("\tsurplus users: ",end = "")
for yy2 in yy:
    print(yy2 + "  ",end = "")
uu = {}
uuflag = True
prompt = "\nplease input your like color: "
prompt += "go on?? "
while uuflag:
    color = input(prompt)
    name = input("what your name? ")
    uu[color] = name
    last = input("Is someone need?yes or no ?")
    if last == 'no':
        uuflag = False
print(uu,end = "")
for color,name in uu.items():
    print("\n" + name + " like to eat " + color + ". ")
    

