#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Apple:
    pass


# In[5]:


class Apple:
    color = ""
    flavor = ""
    
jonagold = Apple()
jonagold.color = "red"
jonagold.flavor = "sour"
 
print(jonagold.color)
print(jonagold.flavor)
print(jonagold.color.upper())


# In[6]:


class Flower:
    color = 'unknown'
rose = Flower()
rose.color = "red"

violet = Flower()
violet.color = "blue"

this_pun_is_for_you = "Sugar is sweet, and so are you"
print("Roses are {},". format(rose.color))
print("Violets are {},". format(violet.color))
print(this_pun_is_for_you)


# In[7]:


class Apple:
    def __init__(self, color, flavor):
        self.color = color
        self.flavor = flavor
jonagold = Apple("red", "sweet")
print(jonagold.color)


# In[13]:


class Apple:
    def __init__(self, color, flavor):
        self.color = color
        self.flavor = flavor
    def __str__(self):
        return "This apple is {} and its flavor is {}".format(self.color, self.flavor)
jonagold = Apple("red", "sweet")
print(jonagold.color)


# In[14]:


class Person:
    def __init__(self, name):
        self.name = name
    def greeting(self):
        __
        print("Hello my name is {name}.".format(name=hy))


# In[16]:


class Fruit:
    def __init__ (self, color, flavor):
        self.color = color
        self.flavor = flavor
class Apple(Fruit):
    pass
class Grape(Fruit):
    pass
granny = Apple("green", "tart")
granny2 = Grape("Purple", "Sweet")
print(granny.flavor)


# In[ ]:




