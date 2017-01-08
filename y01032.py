def make_album(music_name,music_list):
    global x,flag
    if x == 1:
        music1[music_name] = music_list
        print("第一张专辑: name " + music_name + " list " + music_list)
    elif x == 2:
        music2[music_name] = music_list
        print("第二张专辑: name " + music_name + " list " + music_list)
    elif x == 3:
        music3[music_name] = music_list
        print("第三张专辑: name " + music_name + " list " + music_list)
        music = [music1,music2,music3]
        print(music,end = "")
        print("输入三张专辑完毕！")
        x = 0
        flag = False
    else:
        print("输入三张专辑完毕！")
flag = True
x = 0
music1 = {}
music2 = {}
music3 = {}
music = []
while flag:
    x = x + 1
    yy1 = input("请输入歌名： ")
    yy2 = input("请输入专辑： ")
    make_album(yy1,yy2)

