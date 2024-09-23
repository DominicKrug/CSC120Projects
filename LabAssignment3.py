#!/usr/bin/env python
# coding: utf-8

# In[46]:


# Seeing if someone is Elligible to vote
Age = int(input("Your age:"))
Citizenship = input("your citizenship:")
if Citizenship in ["United States", "America"] and Age > 17:
        print("You are eligible to vote")
else: 
    print("You are not eligible to Vote")


# In[19]:


# seeing if year is a leap year
year = int(input("Year:"))
print("is a Leap year" if (year % 400 == 0) or (year % 100 == 0 and year % 4 == 0) or (year % 4 == 0) else "is not a leap year")


# In[17]:


# checking if password is correct
Correct_password = "L4bAssignment!"
Correct_password = (input("password:"))
if Correct_password == "L4bAssignment!": 
        print("Correct Password")
else: print("Wrong password")


# In[63]:


# Input month, and see how many days in it
def days_in_month(month):
    months = ["January", "February", "March", "April", "May", "June", 
              "July", "August", "September", "October", "November", "December"]
    days = [31, "28/29", 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if month in months:
        index = months.index(month)
        print(f"The number of days in {month} is {days[index]} days")
    else:
        print("Invalid month name")

month_input = input("Enter a month name: ")
days_in_month(month_input)


# In[60]:


# Find sum of numbers 1-20
x = sum(range(1, 21))
print(x)


# In[61]:


# Finding smallest number in list
i = [3,9,1,6,2,8]
a=i[0]
for b in i:
    if a > b:
        a=b
print(a)


# In[77]:


# numbers between 100 and 500 that are divisible by 11 but not by 2
numbers = []

for x in range(100, 501): 
    if x % 11 == 0 and x % 2 != 0: 
        numbers.append(x)

print(numbers)


# In[111]:


# sum of all positive numbers in list
numbers = [-2, 13, -4, -5, -6, 10, 20, 30, -12]
sum = 0
for num in numbers:
    if num > 0:  
        sum += num print(sum)


# In[134]:


# print all numbers 1 to 30 that are not devisible by 5,10,15
for num in range(1, 31): 
    if num % 5 != 0:  
        print(num)  


# In[159]:


# Converting centimeters to inches unless their negative
Centimeters = float(input("When Centimeters are"))
Inches = Centimeters / 2.54
if Centimeters < 0:
    print("entry is invalid")
else:
    print ("inches are", Inches, "inches")


# In[ ]:




