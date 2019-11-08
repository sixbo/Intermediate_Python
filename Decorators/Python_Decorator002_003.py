#多个装饰器装饰一个函数
import  time
def deco (func):
    def wrapper(*arges,**keyarges):
        print("这是第一个装饰器")
        start_time=time.time()
        func(*arges,*keyarges)
        end_time=time.time()

        execution_time=(end_time - start_time)*1000
        print("执行时间 %d ms"%execution_time)
    return wrapper

def deco02(func):
    def wrapper(*args,**keyarges):
        print("这个是第二个装饰器")

        start_tiem=time.time()

        func(*args,**keyarges)
        end_tiem=time.time()
        print("第二个就是玩")
    return wrapper

@deco
#@deco02
def f(a,b):
    print("hello")
    time.sleep(1)
    print("a+b %d=" %(a+b))
'''@deco
@deco02
def f2(a,b,c):
    print("a:",a)
    print("b:",b)
    print("c:",c)'''



if __name__ =='__main__':
    f(3,4)
   # x={"name":12,"sge":18,"sex":12}
    #f2(**x)
'''
这里的deco函数就是最原始的装饰器，他的参数是一个函数func，然后返回也是一个函数 wrapper
其中作为参数的这个函数func()就在返回函数内部执行。然后再函数f()前main加上@deco,
f()函数就相当于注入了计时功能，现在只要调用f()他就已经变身为新的功能更多的函数了。不需要重复执行原函数可以节省很多资源。

装饰器调用顺序

装饰器是可以叠加使用的，那么使用装饰器以后代码是啥顺序呢？

对于Python中的”@”语法糖，装饰器的调用顺序与使用 @ 语法糖声明的顺序相反。

在这个例子中，”f(3, 4) = deco01(deco02(f(3, 4)))”
'''