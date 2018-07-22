"""
*args 与 **kwargs不定长参数的装包与拆包
    1. 装包，针对的是形参中的*args、**kwargs
       通过'*'告诉python解析器 把调用者传递过来的没有变量接收的未命名参数，装在args这个元组中
       通过'**'告诉python解析器 把调用者传递过来的命名参数，装在kwargs这个字典中
    2. 拆包，针对的是函数体中的*args、**kwargs
      函数体里的args依然是那个元组，但是*args的含义就是把元组中的数据进行拆包，也就是把元组中的数据拆成单个数据
      kwargs同理可知
"""

def task2(a,b,*args,**kwargs):
    print("-------task2----------")
    print(a)
    print(b)
    print(args)
    print(kwargs)

def task1(a,b,*args,**kwargs):
    print("-------task1----------")
    print(a)
    print(b)
    print(args)
    print(kwargs)
    print(*args) #　３　４　　５　６
    # print(**kwargs)  有报错 name='张三'  age=22
    # 需求： 把传递过来的参数原封不动传递到task2函数中
    x=args
    y=kwargs
    task2(a,b,*x,**y)


# 调用函数
task1(1,2,3,4,5,6,name="张三",age=22)