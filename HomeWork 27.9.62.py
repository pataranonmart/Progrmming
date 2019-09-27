#!/usr/bin/env python
# coding: utf-8

# In[10]:


#ข้อที่1.มีกระดุม 50 เม็ด ถ้านำไปติดเสื้อ 24 เม็ดจะเหลือกระดุมกี่เม็ด
a=int(input("มีกระดูม"))
b=int(input("นำกระดูมไปติดเสื้อ"))
print("จะเหลือกระดูม",a-b,"เม็ด")
    
      


# In[1]:


#ข้อที่2.เด็ก 9 คน ได้ขนมคนละ 5 ห่อ รวมเป็นขนมทั้งหมด 
a=int(input("จำนวนเด็ก"))
b=int(input("ได้ขนมคนละ"))
print("เด็กๆจะได้ขนมรวมกัน",a*b,"ห่อ")


# In[6]:


#ข้อที่3.โปรแกรมแปลงจากเลขฐาน 2 เป็นฐาน 10
x = input("Enter binary number: ")
d = len(x)-1
sum = 0
for y in x:
   if y == '1':
      sum = sum+2**d
   d = d-1
print(sum)


# In[7]:


#ข้อที่4.โปรแกรมคำนวณพื้นที่สามเหลี่ยมที่ทราบความยาวด้านสองด้าน (aกับb) และมุมระหว่างด้านสองด้านนั้น(c)
import math
A = float(input("Fill Out A :"))
B = float(input("Fill Out B :"))
D = float(input("Fill Out D :"))
C = D*math.pi/180
c = math.sqrt((a*a)+(b*b)-(2*a*b*math.cos(C)))
print("c =", c, "cm.")


# In[11]:


#ข้อที่5.โปรแกรมแปลงอุณหภูมิ
C = float(input("Fill out C : ") )
F = ((9/5) * C) + 32
K = C +  273.15
print(F, "F")
print(K, "K")


# In[13]:


#ข้อที่6.โปรแกรมรับจำนวนเต็ม 
x = input("Enter number: ")
d = len(x)-1
while d != -1:
   print(x[d])
   d = d-1


# In[2]:


#ข้อที่7.โปรแกรมรับจำนวนเต็มระหว่าง 0 ถึง 9 จากนั้นแสดงแผนภาพฮิสโตแกรมที่แสดงความถี่ของข้อมูลแต่ละตัวที่ได้รับมา
#โปรแกรมจะรับข้อมูลจากผู้ใช้จนกระทั่งผู้ใช้ป้อนข้อมูลที่น้อยกว่า 0
#ในการแสดงฮิสโตแกรมให้แสดงความถี่ด้วยเครื่องหมาย *
x = int(input())
n =[[],[],[],[],[],[],[],[],[],[]]
while x >=0 :
    if x == 0:
        n[0].append('*')
    elif x == 1:
        n[1].append('*')
    elif x == 2:
        n[2].append('*')
    elif x == 3:
        n[3].append('*')
    elif x == 4:
        n[4].append('*')
    elif x == 5:
        n[5].append('*')
    elif x == 6:
        n[6].append('*')
    elif x == 7:
        n[7].append('*')
    elif x == 8:
        n[8].append('*')
    elif x == 9:
        n[9].append('*')
    x = int(input())
for i in range(10):
    sum = ''
    for y in n[i]:
        sum = sum+y
    print(i,":",sum)


# In[1]:


#ข้อที่8.โปรแกรมคิดเงินค่าจอดรถ
import math
print("in-out 7:00 - 23:00")
hoursin = int(input("Fill out hours in :"))
timesin = int(input("Fill out time in :"))
hoursout = int(input("Fill out hours out :"))
timesout = int(input("Fill out time out :"))
totalhours1 = hoursout-hoursin
totalhours2 = totalhours1*60
totaltimes1 = timesout-timesin
total = totalhours2+totaltimes1
if total <=15:
    print("0")
elif total <=360:
    totaltime = math.ceil(total/60)
    if totaltime <=3:
        print(totaltime*10)
    else:
        total3 = totaltime-3
        print(30+total3*20)
else:
    print("200")


# In[3]:


#ข้อที่9.โปรแกรมรับจำนวนเต็ม N และ K จากนั้นพิมพ์เลขตั้งแต่ 1 ถึง N ที่ K หารลงตัว
n = int(input("Enter N: "))
k = int(input("Enter K: "))
for x in range(1,n+1):
   if  x%k == 0:
      print(x)


# In[5]:


#ข้อที่10.ร้านขายหนังสือร้านหนึ่ง พยายามเพิ่มยอดขายโดยการเสนอโปรโมชั่นพิเศษ 
#ถ้าคุณซื้อหนังสือมากกว่า 3 เล่ม ที่มีมูลค่ารวมเกิน 500 บาท คุณจะได้ส่วนลด 10%
#ให้เขียนโปรแกรมรับจำนวนหนังสือที่ซื้อและราคารวม จากนั้นคำนวณราคาที่ต้องจ่าย
count = int(input("How many books: "))
money = int(input("How much: "))
if count > 3 and money > 500:
   s = money-money*0.1
else:
   s = money
print("You have to pay",int(s),"bath.")


# In[ ]:




