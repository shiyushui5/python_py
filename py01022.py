#yy = 0
#while yy <= 10:
#    yy += 1
#    if yy % 2 != 0:
#        continue
#    print (yy,end = "")
prompt = "\nthis is a film:"
prompt += "how old are you? "
yy = ""
while True:
    yy = input(prompt)
    if yy.isdigit():
       yy = int(yy)
    else:
       print("please write right number!")
       continue
    if yy <= 3:
        print("free!,you are too yong!")
        break
    elif yy <= 12:
        print("you need 10 dollar!")
        break
    else:
        print("you too old and need 15 dollar!")
        break
