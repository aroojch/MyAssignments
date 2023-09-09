#!/usr/bin/env python
# coding: utf-8

# In[1]:


def thing():
    print('Hello')
    print('Fun')
thing()
print('Zip')
thing()


# In[1]:


x = 5
print('Hello')
def print_lyrics():
    print("I'm a lumberjack, and I'm okay.")
    print('I sleep all night and I work all day.')
print('Yo')
print_lyrics()
x = x + 2
print(x)


# In[4]:


def addtwo(a, b):
    added = a + b
    return added
print(addtwo(3, 5))


# In[5]:


# exercise solved question

def computepay(hours, rate):
    if hours <= 40:
        pay = hours * rate
    else:
        regular_pay = 40 * rate
        overtime_pay = (hours - 40) * (rate * 1.5)
        pay = regular_pay + overtime_pay
    return pay

# Get user input for hours worked and hourly rate
hours_worked = float(input("Enter hours worked: "))
hourly_rate = float(input("Enter hourly rate: "))

# Calculate the pay using the computepay function
total_pay = computepay(hours_worked, hourly_rate)

# Display the calculated pay
print("Total pay:", total_pay)


# In[ ]:




