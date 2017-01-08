def get_fullname(first,last,middle=''):
    if middle:          #判断字符时，空格表示是真，空字符是什么都没有，表示假
        full_name = first + ' ' + middle + ' ' + last
    else:    
        full_name = first + ' ' + last
    return full_name.title()
