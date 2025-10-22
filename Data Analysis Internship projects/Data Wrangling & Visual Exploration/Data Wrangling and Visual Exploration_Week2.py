#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Importing the necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
import seaborn as sns 
from sklearn.preprocessing import MinMaxScaler


# # LOADING AND CLEANING DATA

# In[2]:


# Loading the data 
# sales_data.csv 

df = pd.read_csv(r"C:\Users\kiran\OneDrive\Desktop\sales_data.csv")
print("\n Sales Dataset")
display(df)


# In[3]:


# product_info.csv 

df1 = pd.read_csv(r"C:\Users\kiran\OneDrive\Desktop\product_info.csv")
print("\n Product Information Dataset")
display(df1)


# In[4]:


# customer_info.csv 

df2 = pd.read_csv(r"C:\Users\kiran\OneDrive\Desktop\customer_info.csv")
print("\n Customer Information Dataset")
display(df2)


# # SALES DATASET

# In[5]:


# Displaying info and missing vales

df.info()
print("Missing values in the sales dataset: \n", df.isnull().sum())


# In[6]:


# Displaying the column options with counts

print("Delivery Status Counts \n", df['delivery_status'].value_counts())
print("Payment Method Counts \n", df['payment_method'].value_counts())
print("Region Counts \n", df['region'].value_counts())


# In[7]:


# Clean spaces first
df['delivery_status'] = df['delivery_status'].str.strip()
df['payment_method'] = df['payment_method'].str.strip()
df['region'] = df['region'].str.strip()


# In[8]:


# Standarising inconsistent text values
# for the column 'delivery_status' - Creating it as a dictionary
df['delivery_status'] = df['delivery_status'].replace({
    'delivered': 'Delivered',
    'DELAYED': 'Delayed', 
    'delrd': 'Delayed',
    'delyd': 'Delayed'
    
})

# for the column 'payment_method'
df['payment_method'] = df['payment_method'].replace({
    'bank transfr': 'Bank Transfer',
    'credit card': 'Credit Card'
})

# for the column 'region'
df['region'] = df['region'].str.replace('nrth', 'North')

display(df)


# In[9]:


# For checking purposes 
print("Delivery Status Counts \n", df['delivery_status'].value_counts())
print("Payment Method Counts \n", df['payment_method'].value_counts())
print("Region Counts \n", df['region'].value_counts())


# In[10]:


# Converting date columns to date-time format
df['order_date'] = pd.to_datetime(df['order_date'])
print("\n Conversion of the 'order_date' column to 'datetime' format")
df['order_date']


# In[11]:


# Filling the 'discount_applied' column of empty values with 0.00
df['discount_applied'] = df['discount_applied'].fillna(0.00)
display(df['discount_applied'])


# In[12]:


# Dropping the rows with empty values in the payment_method and unit_price column 
df = df.dropna(subset=['payment_method']) 
df = df.dropna(subset=['unit_price']) 
df = df.drop_duplicates() 

display(df)


# Dropping the empty values in the 'payment_method'and 'unit_price' column as they are important columns necessary to analyse user behavior. Having empty values in these might distort the analysis or can lead to false interpretations.

# In[13]:


# Checking if the columns - 'discount_applied' and 'unit_price' are non-negative 

discount_applied = df.query("discount_applied < 0")
discount_applied


# In[14]:


unit_price = df.query("unit_price < 0")
unit_price


# No results indicate that all values are non-negative

# # PRODUCT INFORMATION DATASET 

# In[15]:


# Displaying info and missing vales

df1.info()
print("Missing values in the sales dataset: \n", df1.isnull().sum())


# In[16]:


# Displaying the column options with counts

print("Category Counts \n", df1['category'].value_counts())


# In[17]:


# Converting date columns to date-time format
df1['launch_date'] = pd.to_datetime(df1['launch_date'])
print("\n Conversion of the 'launch_date' column to 'datetime' format")
df1['launch_date']


# In[18]:


# Checking if the column -'base_price' are non-negative 
base_price = df1.query("base_price < 0")
base_price


# No results indicate that all values are non-negative

# # CUSTOMER INFORMATION DATASET

# In[19]:


# Displaying info and missing vales

df2.info()
print("Missing values in the sales dataset: \n", df2.isnull().sum())


# In[20]:


# Displaying the column options with counts

print("Gender Counts \n", df2['gender'].value_counts())
print("Loyalty Tier Counts \n", df2['loyalty_tier'].value_counts())
print("Region Counts \n", df2['region'].value_counts())


# In[21]:


# Clean spaces first
df2['gender'] = df2['gender'].str.strip()
df2['loyalty_tier'] = df2['loyalty_tier'].str.strip()
df2['region'] = df2['region'].str.strip()


# In[22]:


# Standarising inconsistent text values
# for the column 'gender' - Creating it as a dictionary
df2['gender'] = df2['gender'].replace({
    'Male': 'male',
    'femle': 'female', 
    'FEMALE': 'female',
    'Female': 'female'
    
})

# for the column 'loyalty_tier'
df2['loyalty_tier'] = df2['loyalty_tier'].replace({
    'GOLD': 'Gold',
    'gold': 'Gold',
    'gld': 'Gold',
    'brnze': 'Bronze',
    'bronze': 'Bronze',
    'sllver': 'Silver',
})

display(df2)


# In[23]:


# Converting date columns to date-time format
df2['signup_date'] = pd.to_datetime(df2['signup_date'])
print("\n Conversion of the 'signup_date' column to 'datetime' format")
df2['signup_date']


# In[24]:


# Dropping the rows with empty values in the region column 
df2 = df2.dropna(subset=['region'])  
df2 = df2.drop_duplicates() 

display(df2)


# Dropping the rows with empty values in the 'region' column as the presence of information in this field is needed to analyse user behavior across regions. 

# # MERGING: 

# In[28]:


# Merging 'sales_data' with 'product_info' using 'product_id'

df3 = pd.merge(df, df1, on="product_id", how = "left")
display(df3)


# In[31]:


# Merging the result with 'customer_info' using 'customer_id'
merged_df = pd.merge(df3, df2, on= "customer_id", how = "left")
print("\n Merged Dataset")
display(merged_df)


# In[33]:


merged_df.info()
merged_df.head()


# # FEATURE ENGINEERING

# In[38]:


# Creation of new features
# revenue = quantity * unit_price * (1-discount_applied)

merged_df["revenue"] = (merged_df["quantity"] * merged_df["unit_price"] * (1- merged_df["discount_applied"]))
merged_df["revenue"]                             


# Error appears as the column 'quantity'is of type object, so the multiplication cannot be done. Hence, converting it into float64 format. 

# In[42]:


# Finding the type of each column
print(merged_df.dtypes)


# In[41]:


# Converting it into numeric 
merged_df['quantity'] = pd.to_numeric(merged_df['quantity'], errors='coerce')


# In[44]:


# Now, creating new column for revenue
# revenue = quantity * unit_price * (1-discount_applied)

merged_df["revenue"] = (merged_df["quantity"] * merged_df["unit_price"] * (1- merged_df["discount_applied"]))
merged_df


# In[46]:


# order_week = ISO week from order_date
merged_df["order_week"] = merged_df["order_date"].dt.isocalendar().week   
merged_df
# To convert to ISO year - df.dt.isocalendar.year()


# In[51]:


# price_band = Categorise unit_price as Low (<£15), Medium (£15–30), High (>£30)
merged_df["price_band"] = merged_df["unit_price"].apply(lambda x: 'Low' if x < 15.0  else 'High' if x > 30 else 'Medium')
merged_df


# In[59]:


# days_to_order = Days between launch_date and order_date 
merged_df["days_to_order"] = merged_df["order_date"] - merged_df["launch_date"]
merged_df


# In[62]:


# email_domain = Extract domain from email (e.g., gmail.com)
merged_df["email_domain"] = merged_df ["email"].str.split('@').str[1]
merged_df


# In[67]:


# is_late = True if delivery_status is "Delayed"
merged_df["is_late"] = merged_df["delivery_status"].apply(lambda x: True if x == "Delayed" else False)
merged_df


# In[75]:


merged_df.columns


# # SUMMARY TABLES

# In[83]:


# Weekly revenue trends by region
revenue_trends = merged_df.groupby('region_x')['revenue'].count()
print("\n Weekly Revenue trends by region")
display(revenue_trends)


# In[82]:


# Product category performance (revenue, quantity, discount_applied) 
performance = merged_df.groupby('category').agg({'revenue': 'sum', 'quantity': 'sum', 'discount_applied': 'sum'})
print("\n Product Category Performance")
display(performance)


# In[92]:


# Adding another column, converting signup_date to signup_month
merged_df["signup_month"] = merged_df["signup_date"].dt.month
merged_df


# In[97]:


# Customer behaviour by loyalty_tier and signup_month
customer_behavior = merged_df.pivot_table(values = 'customer_id', index = 'loyalty_tier', columns = 'signup_month', aggfunc = 'count', fill_value = 0)
print("\n Customer behaviour by loyalty_tier and signup_month")
display(customer_behavior)


# In[98]:


# Delivery performance by region and price_band
delivery_performance = merged_df.pivot_table(values = 'delivery_status', index = 'region_x', columns = 'price_band', aggfunc = 'count', fill_value = 0)
print("\n Delivery performance by region and price_band")
display(delivery_performance)


# In[99]:


# Preferred payment methods by loyalty tier
payments_methods = merged_df.groupby('payment_method')['loyalty_tier'].value_counts().unstack(fill_value = 0)
print("Preferred payment methods by loyalty tier \n")
display(payments_methods)


# # VISUAL EXPLORATION

# In[101]:


# Line plot - weekly revenue by trends 
weekly_revenue = (
    merged_df.set_index('order_date')['revenue']
             .resample('W')     
             .sum()
)


plt.figure(figsize=(12,6))
plt.plot(weekly_revenue.index, weekly_revenue.values, marker='o')

plt.title("Weekly Revenue Trend")
plt.xlabel("Week")
plt.ylabel("Revenue")
plt.grid(True)
plt.show()


# In[108]:


# Bar chart - top 5 categories by revenue

# Create figure and axis 
fig,ax = plt.subplots(figsize=(12,6))

# Bar plot
bars = ax.bar(merged_df['category'].astype(str), merged_df['revenue'], color = 'skyblue', edgecolor = 'black')

# Titles and labels
ax.set_title("Category by revenue", fontsize=14)
ax.set_xlabel("Category")
ax.set_ylabel("Revenue")

# Light grid lines
#ax.grid(True, axis = 'y', color = 'white')

# Adjust inner padding 
plt.subplots_adjust(left= 0.15, right=0.95, top= 1.58, bottom=0.15)

# Show plot
plt.show()


# In[111]:


# Boxplot - quantity vs discount across categories
# We need to melt the dataframe as we need both quantity and discount across categories
df_melted = merged_df.melt(id_vars="category", value_vars=["quantity", "discount_applied"], 
                           var_name="metric", value_name="value")

plt.figure(figsize=(12,6))
sns.boxplot(x="category", y="value", hue="metric", data=df_melted)
plt.title("Quantity vs Discount Across Categories")
plt.xticks(rotation=45)
plt.show()



# In[114]:


# Heatmap - correlation between revenue, discount, and quantity

corr= merged_df[['revenue', 'discount_applied', 'quantity']].corr()
print(corr)

# Correlation Matrix 
sns.heatmap(corr, annot= True, cmap='coolwarm', linewidths=0.6)
plt.title("Correlation Heatmap")
plt.tight_layout()
plt.show()


# In[118]:


# Countplot - orders by loyalty tier (with hue = region)
sns.countplot(x='loyalty_tier', hue = 'region_x', data = merged_df, palette = 'Set2')
plt.title("Orders by loyalty tier")
plt.tight_layout()
plt.show()


# In[ ]:


# Stacked bar or pie - delivery status by price band

bands = ['Low', 'Medium', 'High']
delivery_performance = delivery_performance.reindex(columns=bands, fill_value=0)

ax = delivery_performance.plot(kind='barh', stacked=True, figsize=(10,6))
ax.set_title('Delivery status by Region and Price Band')
ax.set_xlabel('Number of Deliveries')
ax.set_ylabel('Region')
ax.legend(title='Price Band', bbox_to_anchor=(1.02, 1), loc='upper left')
plt.tight_layout()
plt.show()


# # BUSINESS QUESTIONS

# In[122]:


merged_df.columns


# In[128]:


# 1. Which product categories drive the most revenue, and in which regions

product_categories = merged_df.pivot_table(values = 'revenue', index = 'category', columns = 'region_x', aggfunc = 'count', fill_value = 0)
print("\n Product Categories that drive the most revenue among the regions in UK")
display(product_categories)


# In[138]:


# 2. Do discounts lead to more items sold? 

discounts = merged_df.pivot_table(values = 'quantity', index = 'discount_applied', aggfunc = 'sum', fill_value = 0)
print("\n Does discounts lead to more items sold?")
display(discounts)


# In[141]:


# 3. Which loyalty tier generates the most value?

loyalty_tier = merged_df.pivot_table(values = 'revenue', index = 'loyalty_tier', aggfunc = 'sum', fill_value = 0)
print("\n Which loyalty tier generates the most value?")
display(loyalty_tier)


# In[148]:


# 4. Are certain regions struggling with delivery delays?

regions_df = merged_df.pivot_table(values = 'quantity', index = 'region_x', columns = 'delivery_status', aggfunc = 'count', fill_value = 0)
print("\n Are certain regions struggling with delivery delays?")
display(regions_df)

df_delayed = regions_df[['Delayed']]
display(df_delayed)


# In[150]:


# 5. Do customer signup patterns influence purchasing activity?

signup_revenue = merged_df.groupby("signup_month")["revenue"].sum()
print("\n Customer signup month versus revenue")
print(signup_revenue)

signup_quantity = merged_df.groupby("signup_month")["quantity"].sum()
print("\n Customer signup month versus quantity")
print(signup_quantity)

