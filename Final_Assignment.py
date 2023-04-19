import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('C:\\Users\chris\\Desktop\\liquor_sales_table_2016_2019.csv')

sales_per_zip_code = df.groupby(['zip_code', 'item_description']).sum()['bottles_sold'].reset_index()
print(sales_per_zip_code)

sales_per_store = df.groupby(['store_number','store_name']).sum()['sale_dollars'].reset_index()
sales_per_store['sales_percentage'] = sales_per_store['sale_dollars'].apply(lambda x: (x/df['sale_dollars'].sum())*100)
print(sales_per_store)

plt.scatter(df['zip_code'], df['bottles_sold'], c=df['zip_code'])
plt.title("Bottles Sold")
plt.xlabel("Zip Code")
plt.ylabel("Bottles Sold")
plt.show()

sns.barplot(data=sales_per_store.sort_values('sales_percentage'), y='store_number', x='sales_percentage', orient='h')
plt.title("Sales Percentage per Store")
plt.ylabel("Store Number")
plt.xlabel("Percentage of Total Sales")
plt.show()

plt.scatter(data=sales_per_store.sort_values('sales_percentage'), y='store_number', x='sales_percentage', s='sales_percentage')
plt.title("Sales Percentage per Store")
plt.ylabel("Store Number")
plt.xlabel("Percentage of Total Sales")
plt.show()
