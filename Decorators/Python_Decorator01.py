''''#定义一个函数
def a_new_decorator(a_func):
    def wrapTheFunction():
        print("在执行之前，我正在做一些无聊的操作")
        a_func()

        print("我正在做一些无聊的工作后，执行操作")
    return wrapTheFunction

def a_function_requiring_decoration():
    print("我是需要一些装饰来移除的功能操作")

a_function_requiring_decoration()#直接调用改函数直接打印出：“我是需要一些装饰来移除的功能”
'''
#把函数a_function_requiring_decoration作为一个函数参数传给a_new_decorator执行顺序
#1，先到wrapTheFunction 执行打印：“在执行之前，我正在做一些无聊的工作操作”
#2.a_func()=a_function_requiring_decoration()所以打印“我是需要一些装饰来移除的功能操作”
#3.打印“我正在做一些无聊的工作后，执行操作”
'''
a_function_requiring_decoration=a_new_decorator(a_function_requiring_decoration)

a_function_requiring_decoration()
'''
from  functools import wraps
def a_new_decorator(a_func):
    @wraps(a_func)
    def wrapTheFunction():
        print("在执行之前，我正在做一些无聊的操作")
        a_func()

        print("我正在做一些无聊的工作后，执行操作")

    return wrapTheFunction
@a_new_decorator
def a_function_requiring_decoration():
    """hi  ,来给我装饰一下"""
    print("我是需要一些装饰的功能"
          "清除我的臭味")

a_function_requiring_decoration()

print(a_function_requiring_decoration.__name__)



