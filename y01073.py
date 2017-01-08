mes = "i am a big pigs!"
mes_new = mes.replace('pig','dog')     #替换语句不能替换到原变量中，生成一个新的变量中
print(mes_new,end ="")
file_name = 'y01073h.txt'
with open(file_name,'w') as file_object: #将file_name这个文件写入模式,必须要'w'这个字符,假如没有这个文件，python会自动创建
    file_object.write("i am a so stupid pig!\t")
    file_object.write("i am a so stubbish dog!too!")
with open(file_name) as file_object:    #默认是以 只读模式打开，如果系统没有，则会显示文件出错，并不会创建   
    mes = file_object.read()           #读file_name这个文件的内容
    print(mes)
with open(file_name,'a') as file_object:
    file_object.write("\ni am a real person!")
    file_object.write("you are not!")
test_name = "test.txt"
def count_file(test_name):
    try:
        with open(test_name) as file_test:
            title = file_test.read()
    except FileNotFoundError:
        #mesg = "Sorry,the file " + test_name + " does not exit."
        #print(mesg,end = "")
        pass                              #当产生错误的时候，不执行和语句，跳过执行下一个数值
    else:
        #print(test,end = "")
    #title = "alice in wonderland"
        #print(title,end = "")
        title_divide = title.split()        #将文本分解成单个字符存储在数组里面
        print(title_divide,end = "")
        number_title = 1
        number_t = len(title_divide)
        for title_div in title_divide:
            title_div = title_divide.pop()  #title.reverse（可改变列表的顺序）与pop相对，
            number_title += 1
        print(str(number_t),end = "")
file_names = ["y01073h.txt","y01073w.txt","y01073g.txt"]
for file_name in file_names:              #每次函数只能执行列表中的一个数值，所有要用循环结构
    count_file(file_name)