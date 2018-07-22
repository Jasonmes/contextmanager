

class Goods(object):
    def __init__(self):
        self.__price=4000 # 设置为私有的实例属性，不允许在外部直接修改属性值

    # ----------------------传统方式,定义方法---------------------------

    def get_price(self):
        # 身份验证
        print("get_price")
        return self.__price

    def set_price(self,new_price):
        print("set_price")
        # 验证身份
        # 执行数据的验证
        try:
            self.__price=int(new_price)
        except:
            print("修改价格出错")

    def del_price(self):
        print("del_price")

    """通过类属性方式定义Property属性
    第一个参数是方法名: 获取属性值
	第二个参数是方法名: 设置属性值
    第三个参数是方法名: 删除属性
	第四个参数是字符串: 该属性的描述信息，通过类名.属性名.__doc__调用
    """
    price=property(get_price,set_price,del_price,"商品价格信息")
    # country='zhongguo'


# 使用property属性
goods = Goods()
goods.price=200 # 修改property属性
print(goods.price) # 取得property属性
print(Goods.price.__doc__)
del goods.price

