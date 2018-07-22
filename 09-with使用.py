def filemanager1(file_name):
    file = open(file_name, 'w')
    file.write("C")
    file.close()


def filemanager2(file_name):
    try:
        file = open(file_name, 'w')
        file.write("B")
    except:
        pass
    finally:
        file.close()


def filemanager3(file_name):
    with open(file_name, 'w') as f:
        # 主要业务的实现
        f.write("A")


# 第一种创建写数据到文件
filemanager1("/home/python/Desktop/one.txt")


# 第二种创建写数据到文件
filemanager2("/home/python/Desktop/two.txt")


# 第三种创建写数据到文件
filemanager3("/home/python/Desktop/three.txt")