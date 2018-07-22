"""
property的好处就是 将一个属性的操作方法封装为一个属性，用户用起来就和操作普通属性完全一致,非常简单
"""

class Goods(object):
    def __init__(self):
        self.__price=4000 # 设置为私有的实例属性，不允许在外部直接修改属性值



    # ----------------------使用property方法 定义属性---------------------------
    @property
    def price(self):
        print("取得property属性值")
        # 身份验证
        return self.__price

    @price.setter
    def price(self, new_price):
        # 验证身份
        # 执行数据的验证
        print("设置property属性值:price.setter")
        try:
            self.__price = int(new_price)
        except:
            print("修改价格出错")

    @price.deleter
    def price(self):
        print("删除property属性： price.deleter")









# ----------------------使用property属性---------------------------
p_goods=Goods()
print(p_goods.price)  # 获取property属性值
p_goods.price=3600  # 修改property属性值
print(p_goods.price) # 获取property属性值

del p_goods.price
