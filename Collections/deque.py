from collections import deque

d=deque()

d.append('1')
d.append('2')
d.append('3')
print(d)
print(d[0])

#从两端删除数据

f=deque(range(5))
print(f)
f.popleft()
print(f)
#删除左边数
f.pop()
print(f)
#删除 右边数
'''
我们也可以限制这个列表的⼤⼩，当超出你设定的限制时，数据会从对队列另⼀端被挤出 去(pop)。 
最好的解释是给出⼀个例⼦：
 d = deque(maxlen=30)
现在当你插⼊30条数据时，最左边⼀端的数据将从队列中删除。 你还可以从任⼀端扩展这个队列中的数据
'''
g=deque(range(31))
print(g)
#输出：deque([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30])
#默认把最左边的数字删除
g=deque(range(31),maxlen=30)
print(g)
#输出：deque([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30], maxlen=30)
g.append(88)
print(g)
#输出：deque([2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 88], maxlen=30)
#使用extendleft在左边添加数值，右边自动删除一个数值
g.extendleft([99])
print(g)
g.extend([100])
print(g)
#使用extend在右边添加一个数，左边自动删除一个