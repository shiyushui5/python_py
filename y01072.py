#python只在python_py下的test文件夹内取查找
#with open('test\y01072f.txt') as file_object:
#file_path = r"C:\Desktop\test\y01072f.txt"  r" "表示此路径不是为window设计的
file_path = "C:\\Desktop\\test\\y01072f.txt" #用双\\就不会出错
with open(file_path) as file_object:
    #contents = file_object.read()         #此时这个文件已经关闭了，后面已都都取不到
    #print(contents.rstrip(),end = "")
    #print("ok!")
    lines = file_object.readlines()

    #for line in lines:                     #将每一行都存在变量lines中
    #    print(line,end = "")
pi_str = ''                            #用来存储圆周率的空字符串
for line in lines:
    pi_str += line.strip()            #python将所有的文本解读为字符串，可用int或者float函数转换成整数和浮点数
print(pi_str.rstrip(),end = "")
print(len(pi_str))
file_path = r"C:\Desktop\test\y01072e.txt" 
with open(file_path) as file_object:
    lines = file_object.readlines()
pi_str = ''                            #用来存储圆周率的空字符串
for line in lines:
    pi_str += line.strip()
print(pi_str[2:45] + "...")
birthday = input("please input your birthday： ")
if birthday in pi_str:
    print("your birthday is in the pi_str!")
else:
    print("your birthday is not!")
