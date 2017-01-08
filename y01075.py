line = "dog Dog,jih dog,pig,dog dog dog"
line_count = line.lower().count('dog')     #计算列表中的某字符的个数，区分大小写
print(str(line_count),end = "")
import json
number = [1995,1,12,3132]               #输入的数值的前面的不能是0，不能有空格，除非字符
number1 = [1994,5,23,5213]
filename = 'y01075f.json'
with open(filename,'w') as f_id:
    json.dump(number,f_id)             #json.dump将数据写入文件之中

import json
filename = 'y01075f.json'
with open(filename) as f_id:
    numbers = json.load(f_id)           #json.load加载存储在文件之中的数据
print(numbers,end = "")
