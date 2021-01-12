# 1 增加
def add():
    # 创建空列表
    topData = []
    # 打开数据库
    file = open("src/database/newdata.hdb")
    # 读入数据库至列表并关闭文件
    data = file.read()
    topData = data.split("\n")
    file.close()
    # 数据库为空的情况
    if topData == ['']:
        print("电影排行榜暂无。请先添加！")
    else:
        name = str(input("请输入需要需要添加的电影名称\n>>"))
        position = str(input("请输入需要添加的位置（输入其他值或错误值可退出功能）\n>>"))
        if position.isdigit():
            try:
                # 清空数据库
                topData[int(position) - 1] = name
                file = open("src/database/newdata.hdb", "w")
                file.write("")
                file.close()
                # 将列表中的数据重新写入数据库
                file = open("src/database/newdata.hdb", "a")
                for i in range(0, len(topData), 1):
                    file.write(topData[i] + "\n")
                file.close()
            except:
                print("已退出程序！")
        else:
            print("已退出该功能！")
