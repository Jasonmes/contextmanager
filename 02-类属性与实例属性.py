class Province(object):
    country="中国"# 类属性
    def __init__(self,name):
        self.name=name # 实例属性

    def other_fun(self):
        pass

# 构建实例对象
p1=Province("广东")
print(p1.name) # 实例属性

# 构建实例对象
p2=Province("广西")
print(p2.name) # 实例属性


# 通过类名调用类属性
print(Province.country)

#　可以用实例对象调用类属性，不建议用实例对象方法类属性
print(p1.country)
p1.country='china'  # 在实例对象创建一个实例属性
print(p1.country)
print(Province.country)
