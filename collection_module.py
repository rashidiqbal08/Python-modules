
# #1.namedtuple()
from collections import namedtuple as nt
a=nt('Courses','Language, Duration')
s=a('Python','2 Months')

#providing value by list
l=['java','3 months']
s=a._make(l)
print(s)


#2.deque()
from collections import deque
l=[1,2,3,4]
d=deque(l)
#all the updatation method are quite faster than list add/upd method
d.append(5)
d.appendleft(0)
print(d)
d.pop()
d.popleft()
print(d)   


#3.ChainlMap()
#it is used for combine two dictionary
# Chainmap(a,b)


#4.Counter()   
#it is used to count the occurance of the elements
from collections import Counter
l=[1,2,3,4,2,3,2,1,1,3]

print(Counter(l))
print(list(Counter(l).elements()))