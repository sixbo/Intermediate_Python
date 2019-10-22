# Map会将⼀个函数映射到⼀个输⼊列表的所有元素上 规范   map(function_to_apply,list_of_inputs)
items=[1,2,3,4,5]
squared=[]
'''for i in items:

    #append()在列表后添加一个值
    squared.append(i**2)
    print(squared)'''
squared=list(map(lambda x: x**2,items))

print(squared)

def multiply(x):
    return (x*x)
def add(x):
    return (x+x)

funcs=[multiply,add]
for i in range(5):
    value =list(map(lambda x:x(i),funcs))
    print(value)