#!/usr/bin/env python
# coding: utf-8

# In[2]:


fhand = open('r.txt')
print(fhand)


# In[4]:


xfile = open('r.txt')
for lines in xfile:
    print(lines)


# In[5]:


fhand = open('r.txt')
count = 0
for line in fhand:
    count = count + 1
print('Line Count:', count)


# In[28]:


fhand = open('r.txt')
inp = fhand.read()
print(len(inp))

print(inp[75:90])


# In[30]:


a = open('r.txt')
for line in a:
    if line.startswith('I') :
        print(line)


# In[29]:


ma = open('r.txt')
print(ma)


# In[31]:


fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    quit()
count = 0
for line in fhand:
    if line.startswith('I') :
        count = count + 1
print('There were', count, 'subject lines in', fname)


# In[ ]:




