#!/usr/bin/env python
# coding: utf-8

# In[1]:


str1 = "Hello"
str2 = 'there'
bob = str1 + ' ' + str2  # Adding a space between str1 and str2
print(bob)


# In[1]:


name = input('Enter:')
print(name)


# In[2]:


fruit = 'banana'
letter = fruit[1]
print(letter)


# In[3]:


fruit = 'banana'
letter = fruit[1]
print(letter)
x = 3
w = fruit[x - 1]
print(w)


# In[8]:


apple = input()
x = int(apple) - 10
print(x)


# In[9]:


apple = int(input())
x = (apple) - 10
print(x)


# In[10]:


zot ='abc'
print(zot[2])


# In[11]:


fruit = 'banana'
print(len(fruit))


# In[14]:


fruit = input('Enter : ')
print(len(fruit))


# In[16]:


fruit = 'banana'
index = 0
while index < len(fruit):
    letter = fruit[index]
    print(index, letter)
    index = index + 1


# In[18]:


fruit = 'banana'
for letter in fruit:
    print(letter)


# In[23]:


word = 'banana'
count = 0
for letter in word:
    if letter == 'a':
        count = count + 1
print(count)


# In[24]:


s = 'Monty Python'
print(s[0:4])

print(s[6:7])

print(s[6:20])


# In[27]:


a = 'Hello'
b = a + 'There'
print(b)
c = a + ' ' + 'There'
print(c)
d = 'There'
e = a + ' ' + d
print(e)


# In[28]:


stuff = 'Hello world'
type(stuff)

dir(stuff)


# In[29]:


nstr = 'Hello Bob'.replace('Bob','Jane')
print(nstr)


# In[ ]:




