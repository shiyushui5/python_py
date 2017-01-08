#print(5/0)
try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero!")
prompt = ("give me two numbers,and i'll divide them.")
prompt += ("Enter 'a to quit.")
print("prompt")

while True:
    first_num = input("first number: ")
    if first_num == 'a':
        break
    second_num = input("second number: ")
    if second_num == 'a':
        break
    try:                                          #try excep else 代码块
        answer = int(first_num)/int(second_num)
    except ZeroDivisionError:
        print("You can't divide by zero!")
    else:
        print(answer)
