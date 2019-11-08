import  time
def deco (func):
    def wrapper():
        start_time=time.time()
        func()
        end_time=time.time()

        execution_time=(end_time - start_time)*1000
        print("执行时间 %d ms"%execution_time)
    return wrapper

@deco
def f():
    print("hello")
    time.sleep(1)
    print("haha")

if __name__ =='__main__':
    f()
'''
这里的deco函数就是最原始的装饰器，他的参数是一个函数func，然后返回也是一个函数 wrapper
其中作为参数的这个函数func()就在返回函数内部执行。然后再函数f()前main加上@deco,
f()函数就相当于注入了计时功能，现在只要调用f()他就已经变身为新的功能更多的函数了。不需要重复执行原函数可以节省很多资源。

'''