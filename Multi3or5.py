#!/usr/bin/env python
# coding: utf-8

# In[1]:


# นาย ภัทรชนน แสงสุวรรณ 362515241012 EE36241N
number = int(input("enter number :"))
sum = 0
for number in range(1, number):
    if number % 3 == 0 or number % 5 == 0:
        sum = sum + number
print(sum)


# In[ ]:




