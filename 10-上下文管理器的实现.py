class MyFile():
    def __init__(self, file_name, model):
        self.file_name = file_name
        self.model = model

    def __enter__(self):
        # 初始化资源对象，且返回资源对象
        print("上文管理")
        # 创建文件，且返回文件资源
        self.file = open(self.file_name, self.model)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("下文管理")
        #  业务执行完后，在该方法做善后、清理方面的工作
        self.file.close()


with MyFile("/home/python/a.txt",'w') as f:
    print("正文处理")
    f.write("a")
