#!/usr/bin/env python
# coding: utf-8

# In[1]:


x = ('Glenn', 'Sally', 'Joseph')
print(x[2])

y = ( 1, 9, 2 )
print(y)
print(max(y))


# In[2]:


l = list()
dir(l)


# In[3]:


t = tuple()
dir(t)


# In[4]:


(x, y) = (4, 'fred')
print(y)

(a, b) = (99, 98)
print(a)


# In[6]:


d = dict()
d['csev'] = 2
d['cwen'] = 4
for (k,v) in d.items():
    print(k, v)
    
tups = d.items()
print(tups)


# In[8]:


(0, 1, 2000000) < (0, 3, 4)


# In[14]:


( 'Jones', 'Sally', 'Sally') < ('Adams', 'Sam')


# In[15]:


c = {'a':10, 'b':1, 'c':22}
tmp = list()
for k, v in c.items() :
    tmp.append( (v, k) )
print(tmp)


# In[16]:


fhand = open('r.txt')
counts = {}
for line in fhand:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0 ) + 1
        
lst = []
for key, val in counts.items():
    newtup = (val, key)
    lst.append(newtup)
    
lst = sorted(lst, reverse=True)

for val, key in lst[:10] :
    print(key, val)


# In[ ]:




