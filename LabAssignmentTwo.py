#!/usr/bin/env python
# coding: utf-8

# In[59]:


#Celsius to Farenheit Conversion
Celsius = float(input("Enter the temperature in Celsius:"))
Fahrenheit = Celsius * (9/5) + 32
print(Fahrenheit,"degrees", "Fahrenheit")


# In[56]:


#Sum and Average of the Values in the array
count = 0
sum = 0
print('Before', count, sum)
for value in [11,22,33,44,55]:
    count = count + 1
    sum = sum + value
    print(count,sum,value)
print('After', count, sum, sum/count)


# In[62]:


INPUT1=3
INPUT2=5
SUM= INPUT1 ** 2 + INPUT2 ** 2
print(SUM)


# In[74]:


# SI is simple interest, P is pricipal amount, R is rate of interest, T is time
P = float(input("Principal amount:"))
R = float(input("Rate of interest:"))
T = float(input("Time:"))
SI = (P * R * T)/100
print("Simple interest:", SI)


# In[81]:


import math 
R = float(input("Radius ="))
A = math.pi * R **2
print("Area of the circle =", A)


# In[89]:


print("Time conversion from days")
Days = float(input("Days:"))
Hours = Days * 24
Minutes = Hours * 60
Seconds = Minutes * 60
print("Hours:", Hours) 
print("Minutes:", Minutes)
print("Seconds:", Seconds)


# In[100]:


hourly_wage = input('Please enter your hourly wage: ')
hours_worked = input("How many hours did you work this week? ")
print("hourly wage:", hourly_wage)
print("hours worked:", hours_worked)


# In[110]:


width = 17
height = 12.0
print("width//2 =",width//2, type(width//2))
print("width/2.0 =",width/2.0, type(width/2.0))
print("height/3 =",height/3, type(height/3))
print("1+2**5 =",1+2**5, type(1+2**5))


# In[118]:


Weight = float(input("Weight:")) #use Kilograms for this
Height = float(input("Height:")) #use Meters for this

BMI=Weight / Height **2
print("BMI", BMI)


# In[119]:


import getpass

name = getpass.getuser()

print(f"Welcome to Python programming, {name}.")

