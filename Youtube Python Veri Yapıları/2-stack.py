# 6 November 2021 23:27

# sira ve yigin veri yapilari
# lifo 

l=[1,2,4,6,8]

l.append(55)

print(l.pop())

print(l) #yigindan bir sayiyi cikardik pop metoduyla

#%% queue --> popleft 

l2=[13,6,3,78,937,4]

l2.append(3)
#sona eklemeli


# print(l2.popleft()) artık kullanılmıyor

l2.pop(0)
print(l2) #bastakini aldik

#%% Collections Kutphanesi

#deque'da hem lifo hem de fifo
from collections import deque

l3=deque([1,2,3,4,6,7])
l3.append(79)
print(l3.popleft())
#ilk eklenin cıkması-->queue
#son eklenen ilk --> stack

