class Foo(object):
    country="china" # 类属性

    """无意义的类，随意的类"""
    def __init__(self):
        self.name="张三" # 实例属性
        print("__init__")

    def __str__(self):
        # return "无意义的方法str"
        result="name:"+self.name
        return result

    def __del__(self):
        print("__del__",id(self))

    def __call__(self, *args, **kwargs):
        print("为青春打个call")
        return "为自己打个call"


foo = Foo()

print("-------doc---------")
# doc 表示类的描述信息
print(Foo.__doc__)

print("-------__module__,__class__--------")
# __module__:表示当前操作的对象或者类在哪个模块 ，假如运行的是当前的模块，__module__的值就是__main__
# __class__： 表示当前操作的对象的类是什么
print(Foo.__module__) #
# print(Foo.__class__) # 类对象的类 是type
print(foo.__class__)

if __name__ == '__main__':
    print("运行当前的模块")

# 调用其他的模块，测试模块名
import threading
print(threading.Thread.__module__)

import chat

print(chat.My.__module__)

print("-------dict,str--------")
# __dict__: 显示类或对象中的所有属性
# __str__: 如果类中重写了__str__方法，那么在打印 对象 时，输出该方法的返回值
print(Foo.__dict__)
print(foo.__dict__)
foo.name="李四"
print(foo)

print("-------init,del--------")
# __init__: 当类初始化对象时，自动执行该方法
# __del__: 当对象在内存中被销毁时，自动执行该方法
foo2=Foo()

print("-----------call---------")
# __call__: 对象后面加()，会自动执行该魔法方法
#提示： 必须在创建对象的类中添加__call__()方法，表示类的实例对象是能被callable(调用)的
foo3=Foo() #
print(type(Foo)) # Foo类对象的类 是type
print(type(foo3)) # foo3实例对象的类 是Foo
result=foo3()
print(result)


