# 2 删除
def dlt():
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
        print("电影排行榜暂无。请先添加。（又或许您已经将其全部删除？）")
    else:
        for i in range(0, len(topData), 1):
            print("[" + str(i + 1) + "] " + topData[i])
        num = str(input("请输入您需要删除电影的序号（输入其他内容或错误值可退出功能）\n>>"))
        if num.isdigit():
            try:
                # 清空数据库
                del topData[int(num) - 1]
                file = open("src/database/newdata.hdb", "w")
                file.write("")
                file.close()
                # 将列表中的数据重新写入数据库
                file = open("src/database/newdata.hdb", "a")
                for i in range(0, len(topData), 1):
                    file.write(topData[i] + "\n")
                file.close()
                print("删除成功！")
            except:
                print("已退出删除功能！")
        else:
            print("已退出删除功能！")
