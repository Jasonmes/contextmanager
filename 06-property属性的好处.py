"""
property的好处就是 将一个属性的操作方法封装为一个属性，用户用起来就和操作普通属性完全一致,非常简单
"""

class Goods(object):
    def __init__(self):
        self.__price=4000 # 设置为私有的实例属性，不允许在外部直接修改属性值

    # ----------------------传统方式,定义方法---------------------------

    def get_price(self):
        # 身份验证
        return self.__price

    def set_price(self,new_price):
        # 验证身份
        # 执行数据的验证
        try:
            self.__price=int(new_price)
        except:
            print("修改价格出错")

    # ----------------------使用property方法 定义属性---------------------------
    @property
    def price(self):
        print("property")
        # 身份验证
        return self.__price

    @price.setter
    def price(self, new_price):
        # 验证身份
        # 执行数据的验证
        print("price.setter")
        try:
            self.__price = int(new_price)
        except:
            print("修改价格出错")




# 构建对象
# 在外部直接修改实例属性不好
# goods = Goods()
# print(goods.__price)
# goods.price='a'
# print(goods.price)


# 构建对象
# ----------------------传统操作实例属性的方式---------------------------
goods = Goods()
temp=goods.get_price()
print(temp)
goods.set_price(1600)
print(goods.get_price())



# ----------------------使用property属性的方式---------------------------
print("-----------------property-----------------------")
p_goods=Goods()
print(p_goods.price)  # 获取property属性值
p_goods.price=2600  # 修改property属性值
print(p_goods.price) # 获取property属性值
