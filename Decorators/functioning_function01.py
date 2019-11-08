#从函数中返回函数

def hi(name='sixbo'):
    print("now you are inside the hi() function")

    def greet():
        print("now you are inside the greet() function")
    def welcome():
        print("now you are inside the greet() function")

    if name=='sixbo':
        return greet()
    else:return welcome()




x=hi()
print(x)