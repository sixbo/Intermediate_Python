from collections import Counter
colours=(('yasoob','yellow'),('ali','blue'),('arham','green'),('ali','black'),('yasoob','red'),('ahmed','silver'),)
favs=Counter(name for name,colour in colours)
print(favs)

#也可以在利用他统计一个文件，
#eg：
with open('D:\\123.txt','rb')as f:
    line_count=Counter(f)
print(line_count)