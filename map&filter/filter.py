#获得一个-5到5不包括5的列表
number_list=range(-5,5)
#把number_list列表中小于等于0的数筛选出来传给less_than_zero
less_than_zero=list(filter(lambda x:x<=0,number_list))
#这个filter类似一个for循环，但是他是一个内置函数，并且更快
print(less_than_zero)