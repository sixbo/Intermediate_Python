#在函数中定义函数,也就是嵌套函数

def hi(name='sixbo'):
    print("now you are inside the hi() function")

    def greet():
        print("now you are inside the greet() function")
    def welcome():
        print("now you are inside the greet() function")

    print(greet())
    print(welcome())
    print("now you are back in the hi() function")

hi()
