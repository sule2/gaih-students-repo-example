#!/usr/bin/env python
# coding: utf-8

# In[6]:


mylist = [1,2,3,4,5,6,7,8]
mid = len(mylist)//2
mylist[mid:],mylist[:mid] = mylist[:mid],mylist[mid:]
print(mylist)


# In[16]:


n=int(input("Please enter a single digit integer: "))
list1 = list(range(n+1))
even_nums=[i for i in list1 if i%2 ==0]
print(even_nums)

