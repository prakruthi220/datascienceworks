import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv(r'C:\Users\DELL\Desktop\codes\ml_codes\iris_data.csv')
s = df.shape #to check rows and columns
print(s[0])
#print(df.columns) #display column names
c = df.columns
#print(c.dtype) #display type of the columns
df['species'] = df.species.apply(lambda r: r.replace('Iris-','')) # to remove iris- from every element of species
# print(df['species'])
n = pd.value_counts(df['species'])
print(n)
ds = df.describe()
print(ds)
stats_df = df.describe()
stats_df = df.describe()
stats_df.loc['range'] = stats_df.loc['max'] - stats_df.loc['min']

out_fields = ['mean','25%','50%','75%', 'range']
stats_df = stats_df.loc[out_fields]
stats_df.rename({'50%': 'median'}, inplace=True)
print(stats_df)
#mean1 = df.groupby('species').mean()
#median1 = df.groupby('species').median()
#print(mean1)
#print(median1)
mm = df.groupby('species').agg(['median','mean'])
print(mm)
'''
ax = plt.axes()
ax.scatter(df['sepal_length'],df['sepal_width'])
plt.show()
'''
ax = plt.axes()
ax.hist(df['sepal_length'])
ax.set_title('sepal_width_hist')
plt.show()
