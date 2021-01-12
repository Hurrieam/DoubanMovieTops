# 4 查询
def read():
    # 创建空列表
    topData = []
    # 将数据库中数据读入空列表
    file = open("src/database/newdata.hdb")
    data = file.read()
    topData = data.split("\n")
    # 数据库为空的情况
    if topData == ['']:
        print("电影排行榜暂无。请先添加！")
    else:
        # 依次显示
        print("********************\n豆 瓣 电 影 排 行 榜\n   by 快速的飓风\n********************")
        for i in range(0, len(topData), 1):
            print("[" + str(i + 1) + "] " + topData[i])
    file.close()
