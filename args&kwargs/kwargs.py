def greet_me(**kwargs):
    for key,valus in kwargs.items():
        print("{0}=={1}".format(key,valus))

#调用函数greet_me
greet_me(name='sixliu',sex='男',love='seven')