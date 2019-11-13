J='aA'
S='aAAbbbb'
j=set(J)
s=set(S)

w=(j&s)
o=s-w
listo=list(o)
lists=list(S)
count=0
for i in range(len(listo)):
    for j in range(len(lists)):
        if listo[i]==lists[j]:
            count=count+1
print(len(lists)-count)
print(o)
x=s-o
print(x)
#print(len(x)-len(o))