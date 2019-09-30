"""
    multiple line comment
"""

# comment
print("hello")
# floor division
a=13//5
#
#  modulo division
#
b=26%5
# exponcial
c=2**16
print(a, b, c )

s='ah"oj'
print(s, "\n huhuh")

print(s)
print(s, end="")
print(s)

ls='''very long
multiline'''
print(ls )

print(ls *5)

list=['a','bb','ccc','dd']
print(list[1])
print(list[0:2])
list=[['a','bb'],['ccc','dd']]
print(list[1][0])

list=['a','bb','ccc','dd']
print(list)
list.append("ss")
print(list)
list.insert(2,"ii")
print(list)
list.remove("dd")
print(list)
list.sort()
print(list)
del list[3]
print(list)
print(len(list))
print(max(list))
print(min(list))

# tuple
import time
print(time.localtime())

# dictionary
d={'a':1,4:22,'c':44}
print(d)
print(d.get("b"))
print(d.values())
print(d.keys())

# if else elif == != >= <=
a=21
if a>10:
    print("above 10")
elif a > 5:
    print("above 5")
else:
    print("bellow 5")

for i in range(1,5):
    print(i)

nlist=[[1,3,5],[2,6,8]]
for i in len(nlist[1]):
    print(nlist[i])

for i in len(nlist[1]):
    print(i)

# dictionary
d=dict()
d.add()
