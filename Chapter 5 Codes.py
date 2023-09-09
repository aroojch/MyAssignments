#!/usr/bin/env python
# coding: utf-8

# In[2]:


while True:
    line = input('> ')  # Prompt the user to enter a line of text.
    if line == 'done':  # Check if the entered text is equal to 'done'.
        break  # If 'done' is entered, exit the loop.
    print(line)  # If not 'done', print the entered line.

print('Done!')  # Print 'Done!' after exiting the loop.


# In[3]:


while True:
    line = input('> ')
    if line[0] == '#':
        continue  # Skip lines starting with '#'
    if line == 'done':
        break  # Exit the loop when 'done' is entered
    print(line)

print('Done!')


# In[4]:


largest_so_far = -1
print('Before', largest_so_far)
for the_num in [9, 41, 12, 3, 74, 15]:
    if the_num > largest_so_far:
        largest_so_far = the_num
    print(largest_so_far, the_num)
print('After', largest_so_far)


# In[7]:


found = False  # Initialize the 'found' variable to False
print('Before', found)

for value in [9, 41, 12, 8, 74, 3, 10]:
    if value == 3:
        found = True  # Set 'found' to True if 'value' is equal to 3
    print(found, value)

print('After', found)  # Print 'After' followed by the final value of 'found'


# In[10]:


smallest = None  # Initialize the 'smallest' variable to None
print('Before')

for value in [3, 41, 12, 9, 74, 15]:
    if smallest is None:
        smallest = value  # Set 'smallest' to the first value in the list
    elif value < smallest:
        smallest = value  # Update 'smallest' if a smaller value is encountered

    print(smallest, value)

print('After', smallest)  # Print 'After' followed by the final value of 'smallest'


# In[ ]:




