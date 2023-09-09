#!/usr/bin/env python
# coding: utf-8

# In[4]:


x = int(input("Enter an integer: "))

if x == 5:
    print('Equals 5')
if x > 4:
    print('Greater than 4')
if x >= 5:
    print('Greater than or Equals 5')
if x < 6:
    print('Less than 6')
if x <= 5:
    print('Less than or Equals 5')
if x != 6:
    print('Not equal 6')


# In[6]:


x = 5

if x == 5:
    print('Equals 5')
if x > 4:
    print('Greater than 4')
if x >= 5:
    print('Greater than or Equals 5')
if x < 6:
    print('Less than 6')
if x <= 5:
    print('Less than or Equals 5')
if x != 6:
    print('Not equal 6')


# In[8]:


x = 5
print('Before 5')

if x == 5:
    print('Is 5')
    print('Is Still 5')
    print('Third 5')

print('Afterwards 5')
print('Before 6')

if x == 6:
    print('Is 6')
    print('Is Still 6')
    print('Third 6')

print('Afterwards 6')


# In[10]:


x = 5

if x > 2:
    print('Bigger than 2')
    print('Still bigger')
    print('Done with 2')

for i in range(5):
    print(i)
    if i > 2:
        print('Bigger than 2')
        print('Done with i', i)

print('All Done') 


# In[12]:


x = 4
if x > 2:
    print('Bigger')
else:
    print('Smaller')
print('All done')


# In[13]:


x = 0
if x < 2:
    print('small')
elif x < 10:
    print('Medium')
else:
    print('LARGE')
print('All done')


# In[14]:


x = 5
if x < 2:
    print('small')
elif x < 10:
    print('Medium')
else:
    print('LARGE')
print('All done')


# In[15]:


x = 20
if x < 2:
    print('small')
elif x < 10:
    print('Medium')
else:
    print('LARGE')
print('All done')


# In[16]:


x = 57
if x < 2:
    print('Below 2')
elif x >= 2:
    print('Two or more')
else:
    print('Something else')


# In[18]:


astr = 'Hello Bob'
try:
    istr = int(astr)
except:
    istr = -1
print('First', istr)

astr = '123'
try:
    istr = int(astr)
except:
    istr = -1
print('Second', istr)


# In[19]:


astr = 'Bob'
try:
    print('Hello')
    istr = int(astr)
    print('There')
except:
    istr = -1
print('Done', istr)


# In[20]:


rawstr = input('Enter a number:')
try:
    ival = int(rawstr)
except:
    ival = -1
if ival > 0:
    print('Nice work')
else:
    print('Not a number')


# In[22]:


# Get input from the user
hours = float(input('Enter Hours: '))
rate = float(input('Enter Rate: '))

# Calculate the pay
if hours <= 40:
    pay = hours * rate
else:
    regular_pay = 40 * rate
    overtime_pay = (hours - 40) * (rate * 1.5)
    pay = regular_pay + overtime_pay

print('Pay:', pay)


# In[23]:


try:
    hours = float(input('Enter Hours: '))
    rate = float(input('Enter Rate: '))

    if hours <= 40:
        pay = hours * rate
    else:
        regular_pay = 40 * rate
        overtime_pay = (hours - 40) * (rate * 1.5)
        pay = regular_pay + overtime_pay

    print('Pay:', pay)

except ValueError:
    print('Error, please enter numeric input')


# In[ ]:




