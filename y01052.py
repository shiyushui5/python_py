#设计的传递函数
def print_mol(unprint_model):
    while unprint_model:
        current_mod = unprint_model.pop()
        #将未打印的设计依次传到当前的设计
        print (current_mod)
        #将当前的设计传到一个数组当中
        com_mol.append(current_mod)
def show_des(com_dels):
    #打印好的所有模型都显示出来
    print("the follows is current design:  ")
    print (com_dels)
    for com_del in com_dels:
        print("当前的设计： " + com_del)
tab = 0
unprint_model = []
com_mol = []
flag = True
while flag:
    tab += 1
    input_model = input("please input model: ")
    unprint_model.append(input_model)
    if tab == 3:
        print(unprint_model)
        print_mol(unprint_model[:])
        show_des(com_mol)
        print(unprint_model)
        flag = False

    
    
        
