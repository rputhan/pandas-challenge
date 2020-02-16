#!/usr/bin/env python
# coding: utf-8

# ### Note
# * Instructions have been included for each segment. You do not have to follow them exactly, but they are included to help you think through the steps.

# In[1]:


# Dependencies and Setup
import pandas as pd

# File to Load (Remember to Change These)
file_to_load = "Resources/purchase_data.csv"

# Read Purchasing File and store into Pandas data frame
purchase_data = pd.read_csv(file_to_load)


# ## Player Count

# * Display the total number of players
# 

# In[2]:


total_players = purchase_data["SN"].nunique()
summary_total_players = pd.DataFrame({"Total Players": [total_players]})
summary_total_players


# ## Purchasing Analysis (Total)

# * Run basic calculations to obtain number of unique items, average price, etc.
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display the summary data frame
# 

# In[3]:


unique_items = purchase_data["Item ID"].nunique()
average_price = purchase_data["Price"].mean()
number_of_purchases = purchase_data["Purchase ID"].count()
total_revenue = purchase_data["Price"].sum()
purchasing_analysis = pd.DataFrame({"Unique Items": [unique_items],
                                    "Average Price": [average_price],
                                    "Number of Purchases": [number_of_purchases],
                                    "Total Revenue": [total_revenue]})
purchasing_analysis
                                    


# ## Gender Demographics

# * Percentage and Count of Male Players
# 
# 
# * Percentage and Count of Female Players
# 
# 
# * Percentage and Count of Other / Non-Disclosed
# 
# 
# 

# In[4]:


grouped_gender_df = purchase_data.groupby(['Gender'])
gender_count = grouped_gender_df["SN"].nunique()
gender_percent = gender_count  / total_players * 100

gender_demographics = pd.DataFrame({"Total Count": gender_count,
                                    "Percentage of players":gender_percent})
gender_demographics.head()


# 
# ## Purchasing Analysis (Gender)

# * Run basic calculations to obtain purchase count, avg. purchase price, avg. purchase total per person etc. by gender
# 
# 
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display the summary data frame

# In[5]:


grouped_gender_df = purchase_data.groupby(['Gender'])
purchase_count = grouped_gender_df["SN"].count()
total_purchase_value = grouped_gender_df["Price"].sum()
average_purchase_price = total_purchase_value / purchase_count
average_purchase_per = total_purchase_value / gender_count
gender_analysis = pd.DataFrame({"Purchase Count": purchase_count,
                                "Total Purchase Value":total_purchase_value,
                                "Average Purchase Price":average_purchase_price,
                                "Average Total Purchase Per Person":average_purchase_per})
gender_analysis.head()
                                                                




# ## Age Demographics

# * Establish bins for ages
# 
# 
# * Categorize the existing players using the age bins. Hint: use pd.cut()
# 
# 
# * Calculate the numbers and percentages by age group
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Optional: round the percentage column to two decimal points
# 
# 
# * Display Age Demographics Table
# 

# In[6]:


bins = [0, 9, 14, 19, 24, 28, 33, 39, 100]
group_names = ["<10", "10-14", "15-19", "20-24", "25-29", "30-34", "35-39", "40+"] 


# ## Purchasing Analysis (Age)

# * Bin the purchase_data data frame by age
# 
# 
# * Run basic calculations to obtain purchase count, avg. purchase price, avg. purchase total per person etc. in the table below
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display the summary data frame

# In[7]:


purchase_data["Age Group"] = pd.cut(purchase_data["Age"], bins, labels=group_names)
purchase_data.head()


# ## Top Spenders

# * Run basic calculations to obtain the results in the table below
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Sort the total purchase value column in descending order
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display a preview of the summary data frame
# 
# 

# In[8]:


age_grouped = purchase_data.groupby(['Age Group'])
age_grouped.head()


# ## Most Popular Items

# * Retrieve the Item ID, Item Name, and Item Price columns
# 
# 
# * Group by Item ID and Item Name. Perform calculations to obtain purchase count, item price, and total purchase value
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Sort the purchase count column in descending order
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display a preview of the summary data frame
# 
# 

# In[ ]:





# ## Most Profitable Items

# * Sort the above table by total purchase value in descending order
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display a preview of the data frame
# 
# 

# In[ ]:




