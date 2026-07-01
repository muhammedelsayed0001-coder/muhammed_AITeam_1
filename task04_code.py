import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv("Zara_sales_EDA.csv", sep=';')

df.info()
df.describe()
                                
print(df.head())
print(df.shape)  # seeing  info                      info abt data [ str = [0 , 16 ] - {0,5,10 } colums (int)  ]

print(df.isnull().sum())  # counting the NaN  data    
# name = 1 , description = 2 

# Note  there is no duplicated data :)
print(df.duplicated().sum()) # counting the duplicated data

df = df.dropna(subset=['name', 'description'])     # to delete the Nan values 
print(df.isnull().sum()) # Since there is no missing data, the target data will not be lost
print(df.shape) 

# show the data in order    
df.drop('url', axis=1, inplace=True) # there are data that can be used from it but i will be foucusing on the main data 

for i, col in enumerate(df.columns, start=0):
    print(f"{i} - Column: {col}")
    print(f"Type: {df[col].dtype}")
    print(df[col].describe(include='all'))
    print("=" * 50)


# ---------------- 1- histplot ( Distribution of Zara Prices ) ------------------------------------------

plt.figure(figsize=(10, 6)) 
sns.histplot(data=df, x='price', kde=True, color="#2a8c9d", bins=35)
plt.title('Distribution of Zara Prices', fontsize=16, fontweight='bold', pad=20)
plt.xlabel('Price (USD)', fontsize=12)
plt.ylabel('Count', fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.7) 

plt.show()



# -------------- 2- boxplot ( unique values ) --------------------

plt.figure(figsize=(10, 6))
sns.boxplot(data=df, y='price', color='lightcoral')
plt.title('unique values')
plt.ylabel('(USD)')
plt.tight_layout()
plt.grid(axis='y', linestyle='--', alpha=0.7) 

plt.show()


# ------------------ 3- scatterplot ( Sales Volume vs Price by Section ) ---------------------------


sns.scatterplot(data=df, x="price", y="Sales Volume", hue="section", 
                palette="viridis", s=80, alpha=0.7)

plt.title('Sales Volume vs Price by Section', fontsize=16, fontweight='bold')
plt.xlabel('Price (USD)')
plt.ylabel('Sales Volume')
plt.legend(title='Category', bbox_to_anchor=(1, 1)) 
plt.tight_layout()
plt.show()

# -------------- 4- stripplot ( Price distribution by Product Position and Section ) -----------------

sns.stripplot(x="price", y="Product Position", data=df, hue="section", palette="YlGn")
plt.title("Price distribution by Product Position and Section")
plt.show()
plt.figure(figsize=(10, 6))

# --------------- 5- heatmap ( Zara Dataset )   ----------------------

sns.heatmap(df.corr(numeric_only=True), annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Correlation Heatmap - Zara Dataset")
plt.show()


#-----------------------------------  regplot ( Trend: Price vs Sales Volume )  ------------------------

sns.regplot(data=df, x='price', y='Sales Volume', scatter_kws={'alpha':0.5}, line_kws={'color':'red'})
plt.title(' Trend: Price vs Sales Volume')
plt.xlabel('Price (USD)')
plt.ylabel('Sales Volume')
plt.grid(axis='y', linestyle='--', alpha=0.7) 
plt.show()

