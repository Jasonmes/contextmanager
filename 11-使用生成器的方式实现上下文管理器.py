import contextlib

@contextlib.contextmanager
def my_file(file_name,model):
    print("上文管理")
    # 准备初始化资源，且返回初始化的资源
    f=open(file_name,model)
    yield f
    print("下文管理")
    f.close()


with my_file("/home/python/b.txt",'w') as f:
    print("正文管理-具体的业务，主要的业务")
    f.write("b")