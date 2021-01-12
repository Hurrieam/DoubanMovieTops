# 3 修改
def rewrite():
    # 创建空列表并从数据库读入数据
    topData = []
    file = open("src/database/newdata.hdb")
    data = file.read()
    topData = data.split("\n")
    file.close()
    # 数据库为空的情况
    if topData == ['']:
        print("电影排行榜暂无。请先添加！")
    else:
        name = str(input("请输入需要需要修改的电影名称\n>>"))
        position = str(input("请输入需要修改的位置（输入其他值或错误值可退出功能）\n>>"))
        if position.isdigit():
            try:
                # 清空数据库
                topData[int(position) - 1] = name
                file = open("src/database/newdata.hdb", "w")
                file.write("")
                file.close()
                # 重新从列表读取新数据并写入数据库
                file = open("src/database/newdata.hdb", "a")
                for i in range(0, len(topData), 1):
                    file.write(topData[i] + "\n")
                file.close()
            except:
                print("已退出程序！")
        else:
            print("已退出该功能！")
