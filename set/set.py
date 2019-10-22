#set 函数是无序不重复的元素集合，可以进行关系测试，去除重复数据，还可以计算交集、差集、和并集
#class set（[iterable]）  iterable 可迭代对象

#删除重复
x=set('sixbobo')
y=set('googlebb')
print('删除重复元素',x,y)

#取交集
print(x&y)

#取并集
print(x|y)

#取差集
print(x-y)


some_list=['liubo','liuda','liuer','liusan','liusi','liubo','sixbo','sixbo']

duplicates=[]
for value in some_list:
    #判断列表中A元素的个数大于1
    if some_list.count(value)>1:
        #并且不在变量list中
        if value not in duplicates:
            #添加到列表中
            duplicates.append(value)
print(duplicates)


some_list01=set(['liubo','liuda','liuer','liusan','liusi','liubo','sixbo','sixbo'])

some_list02=set(['liubo','jsj','jdsj'])

#取交集
print(some_list01&some_list02)
print(some_list02.intersection((some_list01))) #intersection交集的方法

#取差集
print(some_list01-some_list02)
print(some_list02.difference(some_list02))#difference 差集
#取并集
print(some_list01|some_list02)
print(some_list02.union(some_list01))#union 并集
