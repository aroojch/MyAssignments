#!/usr/bin/env python
# coding: utf-8

# In[1]:


print(123)


# In[2]:


print(98.6)


# In[4]:


print('Hello World')


# In[5]:


x1q3z9ocd = 35.0
x1q3z9afd = 12.50
x1q3p9afd = x1q3z9ocd * x1q3z9afd
print(x1q3p9afd)


# In[7]:


a = 35.0
b = 12.50
c = a * b
print(c)


# In[11]:


hours = 35.0
rate = 12.50
pay = hours * rate
print(pay)


# In[12]:


print(float(99) + 100)


# In[13]:


i = 42
type(i)


# In[16]:


i = 42
type(i)
f = float(i)
print(f)


# In[17]:


nam = input('Who are you? ')
print('Welcome', nam)


# In[18]:


inp = input('Europe floor?')
usf = int(inp) + 1
print('US floor', usf)


# In[1]:


# Prompt the user for hours worked and hourly rate
hours_worked = float(input("Enter hours worked: "))
hourly_rate = float(input("Enter hourly rate: "))

# Calculate gross pay
gross_pay = hours_worked * hourly_rate

# Display the result
print(f"Gross pay: ${gross_pay:.2f}")


# In[13]:


# Get the name of the file and open it
name = input('Enter file:')
handle = open(name, 'r')


# In[15]:


# Count word frequency
counts = dict()

try:
    # Get the name of the file and open it
    name = input('Enter file:')
    handle = open(name, 'r')

    for line in handle:
        words = line.split()
        for word in words:
            counts[word] = counts.get(word, 0) + 1

    # Print the word frequencies
    for word, count in counts.items():
        print(f"{word}: {count}")

except FileNotFoundError:
    print(f"The file '{name}' does not exist.")
except PermissionError:
    print(f"You do not have permission to open the file '{name}'.")
except Exception as e:
    print(f"An error occurred: {e}")


# In[18]:


# Find the most common word
bigcount = None
bigword = None
for word, count in counts.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count

# Print the most common word and its count
if bigword is not None:
    print(f"The most common word is '{bigword}' with a count of {bigcount}")
else:
    print("No words found in the file.")


# In[20]:


# Get the name of the file and open it
name = input('Enter file:')
handle = open(name, 'r')
# Count word frequency
counts = dict()
for line in handle:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1

# Find the most common word
bigcount = None
bigword = None
for word, count in counts.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count

# All done
print(bigword, bigcount)


# In[ ]:




