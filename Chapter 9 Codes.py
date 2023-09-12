#!/usr/bin/env python
# coding: utf-8

# In[2]:


counts = dict()
print('Enter a line of text:')
line = input('')

words = line.split()

print('Words:', words)

print('Counting...')
for word in words:
    counts[word] = counts.get(word,0) + 1
print('Counts', counts)


# In[5]:


a = dict()
a['Arooj'] = 21
print(a)


# In[ ]:


a = dict()
line = input('Enter a line :')
print(line)

b = line.split()
print(b)

for i in b:
    b[i] = b.get(i,0) + 1
    print(a)


# In[ ]:





# In[ ]:




