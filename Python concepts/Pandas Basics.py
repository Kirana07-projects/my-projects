#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np


# In[3]:


# DataFrame - A two dimentional, labelled data structure in Pandas, similar to a table or a spreadsheet
# Create three DataFrames in three different ways
df1 = pd.DataFrame([[1,2], [3,4]], columns=['A', 'B'])
df2 = pd.DataFrame({'A': [5,6], 'B': [7,8]})   # List Form
df3 = pd.DataFrame(np.random.rand(3,2), columns = ['X', 'Y'])

print("DataFrame 1: \n", df1)
print("DataFrame 2: \n", df2)
print("DataFrame 3: \n", df3)


# In[4]:


# Head and tail function
# Head - to print the first 5 entries by default, unless specified in brackets
# Tail - to print the last 5 entries by default, unless specified in brackets

print("Head Method: \n", df1.head())
print("Tail Mathod: \n", df2.tail(1))


# In[5]:


# info method - it displays a summary of the df's structure including column types and non-null counts

print(df2.info())


# In[6]:


# describe method - it generates descriptive statistics for numeric columns such as mean, median and std.dev

print("Describe Method: \n", df3.describe())


# In[9]:


# to find the location of an entry in a df
# .loc() - label based 
# .iloc() - Position based

print("loc: \n", df3.loc[1, 'Y'])
print("iloc: \n", df3.iloc[1,0])


# In[10]:


# Filtering - based on items, based on 'like' or 'regex' or by row/column indices
# Items - column names

a = df1.filter(items=['B'])
a


# In[11]:


# like - This filters columns whose names contain the letter 'b'.
# The like parameter helps us to match columns based on a substring in their label names.

b = df2.filter(like = 'B', axis = 1)
b 


# In[13]:


# regex - Here, the regular expression [bB] matches any column name that contains
# the letter 'B' or 'b' which allows us to filter columns based on pattern matching.

c = df2.filter(regex = '[bB]', axis = 1)
c 


# In[16]:


# Filtering rows by index labels - filter rows using the axis = 0 parameter

df_filtered_rows = df3.filter(items=[1, 2], axis=0)
print(df_filtered_rows)


# # DATA CLEANING IN PANDAS

# In[40]:


# Reading the Excel file
df = pd.read_excel(r"C:\Users\kiran\Downloads\Customer Call List.xlsx")
df


# If we see the above dataframe, it has a lot of duplicates, missing info, wrong info, not in correct format etc. We need to get rid of these entries as well as the Not_useful_Column and the Do_Not_Contact if yes. This is the first step. 

# In[41]:


# Drop duplicates 

df = df.drop_duplicates()
df


# In[42]:


# Dropping unnecessary columns

df = df.drop(columns = "Not_Useful_Column")
df


# In[43]:


# Stripping off the unnecessary entries from the 'Last_Name' column
# Can be done individually or as a string
#df["Last_Name"] = df["Last_Name"].str.lstrip("...")
#df["Last_Name"] = df["Last_Name"].str.lstrip("/")
#df["Last_Name"] = df["Last_Name"].str.rstrip("_")
df["Last_Name"] = df["Last_Name"].str.strip("123._/")
df


# In[44]:


# Removing all special characters from the 'Phone_Number' column - replacing small a - z, capital A - Z and 
# numbers 0 to 9 with nothing 
df["Phone_Number"] = df["Phone_Number"].str.replace('[^a-zA-Z0-9]', '')
df


# In[47]:


# Formatting it in a way 123-456-7890
df["Phone_Number"] = df["Phone_Number"].apply(lambda x: str(x))

df["Phone_Number"] = df["Phone_Number"].apply(lambda x: x[0:3] + '-' + x[3:6] + '-' + x[6:10])
df


# In[49]:


# Removing the nan-- and Na-- entries

df["Phone_Number"] = df["Phone_Number"].str.replace('nan--','')
df["Phone_Number"] = df["Phone_Number"].str.replace('Na--','')

df


# In[50]:


# Splitting the address for easier visibility 

df[["Street_Address", "State", "Zip_Code"]] = df["Address"].str.split(',', 2, expand = True) # splitting the address with the comma into 2 columns
df

# We can do the same in cases where the name is in the form Lastname, firstname


# In[52]:


# Replacing 'Yes' with 'Y' and 'No' with 'N' to bring uniformity 

df["Paying Customer"] = df["Paying Customer"].str.replace('Yes', 'Y')
df["Paying Customer"] = df["Paying Customer"].str.replace('No', 'N')
df


# In[57]:


# Doing the same for the Do_Not_Contact column

df["Do_Not_Contact"] = df["Do_Not_Contact"].str.replace('Yes', 'Y')
df["Do_Not_Contact"] = df["Do_Not_Contact"].str.replace('No', 'N')
df


# In[59]:


# Getting rid of the N/a and NaN values

df = df.replace('N/a', '')
#df = df.replace('NaN', '')    # This doesn't work as NaN is not a value or a field, so use the fillna command

df = df.fillna('')
df


# In[66]:


# In the Do_Not_Contact column, we must delete the entries which say 'Y' as the customer center shouldn't contact them
# We can't do it like below, as we must look at the row indices

#df["Do_Not_Contact"] = df["Do_Not_Contact"].drop('Y', inplace = True)
#df

# Using row indices and loc
for x in df.index:
    if df.loc[x, "Do_Not_Contact"] == 'Y':
        df.drop(x, inplace = True)
        
df


# In[77]:


# Similarly, drop the rows with empty phone numbers 

# Using row indices and loc
for x in df.index:
    if df.loc[x, "Phone_Number"] == '':
        df.drop(x, inplace = True)
        
df 

# or since we are dropping empty values, we can also do like below; 
# Another way to drop null values 
#df = df.dropna((subset = "Phone_Number"), inplace = True)
#df


# In[68]:


# The index values are not in order, so we must re-order that 
df = df.reset_index(drop = True)
df


# In[79]:


# End of Exercises from the youtube video. 
# Start of Exercises from the course

df1 = pd.DataFrame({'id': [1,2,3], 'birthdate': ['2000-01-01', '1995-05-15', '1988-07-30'], 'category': ['A', 'B', 'A']})
df1


# In[82]:


# Check types
print(df1.dtypes)


# In[85]:


# Convert types
df1['birthdate'] = pd.to_datetime(df1['birthdate'])
df1['category'] = df1['category'].astype('category')

df1


# In[86]:


# Rename and Reorder columns 

df1.rename(columns= {'id': 'ID'}, inplace= True)

df1= df1[['ID', 'category', 'birthdate']]

df1


# In[92]:


# Handling missing and duplicate data
df2 = pd.DataFrame({'A': [1, np.nan, 3, 3], 'B': [4, 5, np.nan, 4]})
df2

# Identifying missing values
print(df2.isnull())
print(df2.isnull().sum())


# In[97]:


# Handle missing values 
df_filled = df2.fillna(0)
print("Filling the NaN values with zeroes \n", df_filled)

df_dropped = df2.dropna()
print("Removed the NaN values based on the index (row) \n", df_dropped)

df_interpolate = df2.interpolate()
print("Interpolate \n", df_interpolate)


# In[98]:


# Handling duplicate records

df3 = pd.DataFrame({'A': [1, 2, 3, 1], 'B': [4, 5, 5, 4]})
df3


# In[99]:


print("Duplicate Rows: \n", df3.duplicated())

# Remove duplicates
df_no_duplicates = df3.drop_duplicates()
print("Cleaned DataFrame \n", df_no_duplicates)

