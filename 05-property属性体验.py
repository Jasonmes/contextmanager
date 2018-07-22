class Foo(object):
    def __init__(self):
        self.name="小张" # 实例属性

    @property
    def prop(self):
        print("property属性") # 执行业务
        return "xxx"


# 构建实例对象
foo = Foo()
print(foo.name)

# 一种用起来像是使用的实例属性一样的特殊属性，可以对应于某个方法，property属性本质还是方法
print(foo.prop)

