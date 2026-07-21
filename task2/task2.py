import pandas as pd
import matplotlib.pyplot as plt # For visualization

df = pd.read_csv("titanic.csv")

print(df.shape)  # seeing the shape 
print(df.isnull().sum())  # counting the NaN  data
print(df.duplicated().sum()) # counting the duplicated data

df['Age'] = df['Age'].fillna(df['Age'].mean())
# filling out NaN  (blanked) values with mean of the age

df.drop(columns=['Cabin'], inplace=True) # removing the cabin for 2 resons 
#1 was missing data and not that important in that case 

df['Embarked'].fillna(df['Embarked'].mode()[0])
 

# Filling missing values with the most frequent value 
# since statistically it has the highest probability of being correct


print(df.isnull().sum()) # Since there is no missing data, the target data will not be lost
print(df.shape)         

chick = df[df['Survived'] == 1]  # chick how many surviving ppl
arranging_data = df.sort_values("Pclass", ascending=True)          # arrange Pclass    

#   visualization 
print (df['Survived'].value_counts())
df['Survived'].value_counts().plot(kind='bar')    
plt.xticks([0, 1], ['Victims', 'Rescued'], rotation=0)
plt.title('Titanic Survivors')
plt.grid(axis='y', linestyle='--', alpha=0.7)  
plt.yticks(range(0, 600, 50))
plt.show()

df['Sex'].value_counts().plot(     # Initial gender split (Pre-incident)
    
    kind='pie',                              
    colors=['#20c9f7', '#fa58fc'],
    autopct='%1.1f%%'              
)
plt.title('Initial gender split (Pre-incident)')
plt.show()

print(round(df['Age'].mean(), 1)) # average age   & take 1 number after the desimal point 
print(df.describe()) # mean , std , IQR ...


sr_after = df.groupby('Sex')['Survived'].mean()*100 # gender split (After-incident)
sr_after.plot(     
    
    kind='pie',                              
    colors=["#f48fed", "#7ff679"],
    autopct='%1.1f%%'              
)
plt.title('gender split (After-incident) ')
plt.show()


survival_rate =df.groupby('Pclass')['Survived'].mean()*100 
survival_rate.plot(     
    kind='pie',
    colors=["#7cfd51", "#f2ef9b","#f39496"],
    autopct='%1.1f%%'              
)
plt.title('Survival rate varies by passenger class')
plt.show()