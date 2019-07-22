#!/usr/bin/env python
# coding: utf-8

# In[4]:


#นาย ภัทรชนน แสงสุวรรณ 362515241012 EE36241N
use=input("Username :")
pas=input("Password :")
if use=="mart" and pas=="2543":
    print("Welcome to Sideline pattaya.")
    print("-------------------Menu-------------------")
    print("1. น้องเจนกระดาน 1000 THB")
    print("2. น้องจังยาวใหญ่  1500 THB")
    print("3. น้องโม้คนมโต 2000 THB")
    print("4. น้องมิ้วขาวใหญ่ 3500 THB")
    print("5. น้องมายอมเก่ง 4000 THB")
    j=1000
    jy=1500
    m=2000
    mi=3500
    ma=4000
    mart=int(input("What do you want?(1-5) : "))
    h=int(input("How many hours do you want? : "))
    if mart==1:
        print("You order ",h," hours with น้องเจนกระดาน ",j*h, " THB")
    elif mart==2:
        print("You order ",h," hours with  น้องจังยาวใหญ่ ",jy*h, " THB")
    elif mart==3:
        print("You order ",h," hours with น้องโม้คนมโต ",m*h, " THB")
    elif mart==4:
        print("You order ",h," hours with น้องมิ้วขาวใหญ่ ",mi*h, " THB")
    elif mart==5:
        print("You order ",h," hours with น้องมายอมเก่ง ",ma*h, " THB")
    
else :
    print("Error I quay.")


# In[ ]:





# In[ ]:




