username,password='sa','123456'

# 当装饰器也需要参入参数时我们需要给装饰器再加一层函数，
# 此时装饰器接受到的方法需要进入第二层函数进行接受，
# 第一层需要接受装饰器自己的参数
def login(login_type):
    def outer_wrapper(func):
        def wrapper(*arg1,**kwargs):
            usernameInput=input("username:").strip()
            passwordInput=input("password:").strip()
            if login_type=='local':
                if username==usernameInput and password==passwordInput:
                    print("登录成功")
                    res=func(*arg1,**kwargs)#接受返回结果
                    return res
                else:
                    print("登录失败")
            elif login_type=='ldap':
                print("远程登录")
        return wrapper
    return outer_wrapper

def index():
    print("欢迎进入这个页面")

@login(login_type='local')
def home():
    print("欢迎进入home的")
    return "from home"

@login(login_type='ldap')
def blog():
    print("欢迎进入blog页面")


#（1） 要想装饰器不修改被装饰函数的返回值，我们需要在装饰器中接受被装饰函数的返回值并Return即可。

#（2） 如果希望对被装饰函数进行分类处理，我们可以在绑定装饰器时传入一个参数用于对被装饰函数进行分类，但是这样我们需要在装饰器中在套一层函数，在第一层接收装饰器传递的参数，在第二层函数中接收被装饰函数。

#（3） 如果希望装饰器既能装饰带参的函数也可以修饰不带参的函数，我们只需要在装饰器中接收参数时，把参数定义为非固定参数即可。


index()

print(home())

blog()


