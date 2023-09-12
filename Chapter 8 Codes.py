#!/usr/bin/env python
# coding: utf-8

# In[1]:


print([1, 24, 76])


# In[2]:


print([ 1, [5, 6], 7])


# In[4]:


for i in [5, 4, 3, 2, 1] :
    print(i)
print('Blastoff!')


# In[6]:


friends = ['Joseph', 'Glenn', 'Sally']
for friend in friends :
    print('Happy New Year:', friend)
for i in range(len(friends)) :
    friend = friends[i]
    print('Happy New Year:', friend) 


# In[7]:


t = [9, 41, 12, 3, 74, 15]
t[1:3]


# In[8]:


stuff = list()
stuff.append('book')
stuff.append(99)
print(stuff)


# In[10]:


abc = 'With three words'
stuff = abc.split()
print(stuff)
print(len(stuff))
print(stuff[0])


# In[ ]:




