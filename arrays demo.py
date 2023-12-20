from array import *
a1=array('i',[10,12,778,-45,0,456])
print(a1)
del a1[2]
print(a1)
s=len(a1)
print('length=',s)
m1=max(a1)
m2=min(a1)
print('max of a1 =', m1,'min of a1 =',m2)
list1=list(a1)
print(list1)
print("count of 10 = ",a1.count(10),"index of 10 =", a1.index(10))

a1.insert(4,5896)
print(a1)

print("updated arrays =",a1.remove(12))
a1.reverse()
print("Reverse of arrays =", a1)


