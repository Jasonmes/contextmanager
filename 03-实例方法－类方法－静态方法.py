class Foo(object):
    def __init__(self):
        self.name="信息"
        print("__init__")

    def instance_fun(self):
        print("实例方法")
        print(self.name)

    @classmethod
    def class_fun(cls):
        print("类方法")

    @staticmethod
    def static_fun():
        print("静态方法")


# 使用实例方法,通过实例对象来调用
foo = Foo()
foo.instance_fun()
foo.class_fun()
foo.static_fun()

# 通过类名调用类方法
Foo.class_fun()
Foo.instance_fun() # 类名不能调用实例方法


# 通过类名调用静态方法
Foo.static_fun()
