#!/usr/bin/env python
# coding: utf-8

# In[70]:


pip install seaborn


# In[71]:


pip install pandas


# In[72]:


pip install matplotlib


# In[73]:


pip install numpy


# In[1]:


#MIDTERM EXAMINATION
#DUE DATE SUNDAY 27TH OCTOBER 11:59
#SAVE THE FILE AS midterms_LASTNAME
#NAME:XXXXX 


# In[2]:


##GENERAL PROGRAMMING
#QUESTION ONE
#Write a function called list_stats that, given a list of numbers, prints the minimum,
#maximum, and average of the numbers in the list. 

def list_stats(list):
    minimum=min(numbers)
    maximum=max(numbers)
    average=sum(numbers)/len(numbers)
    print("the minimum is",minimum,"the maximum is",maximum,"and the average is",average)
     
numbers = [1,3,5,7,11,13,17,19]

list_stats(numbers)


# In[3]:


#QUESTION TWO:
#write a program that prompts the user to enter two positive
#integers w and z ensure that w < b and the prints the list of all 
#perfect squares that are between a and b inclusive

import math
w=int(input("w:"))
z=int(input("z:"))
if w>z:
    print("w must be less than z")
else:
    print('perfect square between',w,'and',z,'are:')
    for num in range(w, z+1):
        if math.isqrt(num)**2 == num:
            print(num)


# In[4]:


#QUESTION THREE:
#Consider the code below and complete it.
#define your own list to test it. 

def doubleList(numberList):
    for num in numberlist:
        print(num*2)
numberlist=[1,3,6,8,15,4]
doubleList(numberlist)


# In[5]:


#QUESTION FOUR:
#Write a python function to find common elements in two lists
# list1 = [1, 2, 3, 4, 5]
# list2 = [4, 5, 6, 7, 8]
# ouput shold be 4

def common_list_elements(list1, list2):
    for element in list1:
        if element in list2:
            return element
list1=[1,2,3,4,5]
list2=[4,5,6,7,8]
common_list_elements(list1,list2)


# In[6]:


#QUESTION FIVE:
#Write a function in python which takes three arguments
#and returns the maximum of the three numbers. 
#do not use max() function

def maximum_of_three(a, b, c):
    if a>b and a>c:
        return a
    elif b>a and b> c:
        return b
    else:
        return c

print(maximum_of_three(1,6,2))


# In[10]:


#QUESTION SIX (indexing and slicing):
#Given the list numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#write the code that does the following
#1. Print the first three numbers
#2. Print the last three numbers
#3. Reverse the list using slicing
list=[1,2,3,4,5,6,7,8,9,10]
print(list[0:3])
print(list[7:10])
print(list[::-1])


# In[11]:


#QUESTION SEVEN:
#Given a dictionary as follows
#write the code to find the student with the highest grade
student_grade = {
    "Jane Doe":75,
    "John Smith":80,
    "George Owell":60,
    "Prince Jeffery":70,
    "Siri Alexa":67
}
top_student=max(student_grade,key=student_grade.get)
highest_grade=student_grade[top_student]
print('The student with the highest grade is',top_student,'with a grade of',highest_grade)


# In[12]:


##EXPLORATORY DATA ANALYSIS
#QUESTION EIGHT:
#Complete the following code

import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns

#1.defining the data
housing_data = pd.DataFrame({
    "income":[200.0, 150.0, 80.0, 120.0, 450.0, 100.0, 500.0, 75.0, 300.0, 350.0],
    "hse_price": [140.0, 90.0, 50.0, 100.0, 450.0, 100 , 200, 180, 150, 200],
    "hse_type": ['sf','th','co','cs', 'rh','sf', 'rh', 'co', 'th','th']
})

#2.performing the basic eda
print(housing_data.info()) #displaying info about the dataframe

print(housing_data.head()) #displaying the first five rows.

#3.descriptive statistics
'''add the code to do it here'''
print(housing_data.describe)
#4.check if there are missing values
'''code goes here'''
print(housing_data.isnull().sum())
#5.five-number statistics summary. 
#use boxplot to do this.
sns.boxplot(x='hse_type', y='hse_price', data=housing_data)
plt.title('House Price Distribution by House Type')
plt.show()

#6.Is there any correlation between income and hse_price
#how will you determine that.
correlation = housing_data['income'].corr(housing_data['hse_price'])
print(f'Correlation between Income and House Price is: {correlation}')
#there is a correlation because it is close to 1


# In[13]:


#QUESTION NINE
#Using the attached data file for cars
#perform an EDA on the data. 
#follow the example during the lecture and the practice sessions

#1.Load libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

df=pd.read_csv('data (1).csv')
print('Check first five sample of data')
print(df.head())
print('general information about the data')
print(df.info())
print('statistical summary of the data')
print(df.describe())
print('check to see missing values in the data')
print(df.isnull().sum())

sns.histplot(df['MSRP'], bins=200, kde=True)
plt.title('Distribution of MSRP')
plt.show()

sns.countplot(y='Make', data=df, order=df['Make'].value_counts().index[:20])
plt.title('Count of Top 20 Car Makes')
plt.show()

df_pplot = df[['Engine HP', 'Number of Doors', 'highway MPG', 'city mpg', 'MSRP']]
sns.pairplot(df_pplot)
plt.suptitle('Pairplot of Car Features', y=1.02)
plt.show()

sns.scatterplot(x='Engine HP', y='MSRP', hue='Vehicle Size', data=df)
plt.title('Engine HP vs MSRP by Vehicle Size')
plt.show()

sns.boxplot(x='Vehicle Size', y='highway MPG', data=df)
plt.title('Highway MPG Distribution by Vehicle Size')
plt.show()

sns.boxplot(x=df['MSRP'])
plt.title('Box Plot of MSRP')
plt.show()

df_corr = df[['Engine HP', 'Number of Doors', 'highway MPG', 'city mpg', 'MSRP']].corr()
sns.heatmap(df_corr, annot=True)
plt.title('Correlation Heatmap of Car Features')
plt.show()

correlation = df['Engine HP'].corr(df['MSRP'])
print(f'Correlation between Engine Horsepower and MSRP is: {correlation}')


# In[14]:


#2.Import the data
df=pd.read_csv('data (1).csv')


# In[15]:


#3. rename the columns
#uncomment the code below and replace...
#the car_data with the variable for your dataframe.

#car_data = car_data.rename(columns={"Engine Fuel Type": "Fuel", "Number of Doors":"Doors", "Engine HP": "HP", "Engine Cylinders": "Cylinders", "Transmission Type": "Transmission", "Driven_Wheels": "Drive Mode","highway MPG": "MPG-H", "city mpg": "MPG-C", "MSRP": "Price" })
#car_data.head(5)

df = df.rename(columns={
    "Engine Fuel Type": "Fuel", 
    "Number of Doors": "Doors", 
    "Engine HP": "HP", 
    "Engine Cylinders": "Cylinders", 
    "Transmission Type": "Transmission", 
    "Driven_Wheels": "Drive Mode",
    "highway MPG": "MPG-H", 
    "city mpg": "MPG-C", 
    "MSRP": "Price"
})
print(df.head(5))


# In[16]:


#4.Inspect the data
print("First five rows of the data:")
print(df.head())
print("\nGeneral information about the data:")
print(df.info())
print("\nStatistical summary of the data:")
print(df.describe())


# In[17]:


#5.Clean the data
#check if there are missing values
print(df.isnull().sum())


# In[18]:


#6.Perform a univariate analysis 
#choose one(numeric) variable
#use histogram to check the distribution
#use box plots to identify outliers

sns.histplot(df['Price'], bins=50, kde=True)
plt.title('Distribution of Car Prices')
plt.xlabel('Price')
plt.show()


# In[19]:


#7.Perform a bivariate analysis
#using Vehicle size and Price
#plot a bar chart 
df.groupby('Vehicle Size')['Price'].mean().plot(kind='bar')
plt.title('Average Price by Vehicle Size')
plt.xlabel('Vehicle Size')
plt.ylabel('Average Price')
plt.show()


# In[67]:


#QUESTION TEN
#determine if there is any correlation between price and popularity
#Can you explain the value 
print(f"The correlation between price and popularity is: {correlation}")
if correlation > 0.5:
    print('Yes, there is a correlation because the correlation value is closer to 1 than 0.')
else:
    print('No, there is not a correlation because the correlation value is closer to 0 than 1.')

