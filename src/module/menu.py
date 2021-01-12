from src.module.add import *
from src.module.dlt import *
from src.module.rewrite import *
from src.module.read import *


# 主菜单
def menu():
    while True:
        print("1 增加电影")
        print("2 删除电影")
        print("3 修改电影")
        print("4 查询电影")
        print("0 退出系统")
        option = str(input("请选择您需要进行的操作\n>>"))
        if option == "1":
            add()
        elif option == "2":
            dlt()
        elif option == "3":
            rewrite()
        elif option == "4":
            read()
        elif option == "0":
            exit(0)
        else:
            print("您的输入有误，请重新输入！")
