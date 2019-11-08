#一切皆对象
def hi(name='sixbo'):
    return 'Hi'     +name
print(hi())

#将函数赋值给一个变量
Y=hi
#不加（）是赋值，加上（）是调用
print(Y())

del hi

#print(hi())
print(Y())