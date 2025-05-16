import pandas as pd
import sklearn.preprocessing as sp
import seaborn as sns
import matplotlib.pyplot as plt


df = pd.read_csv(r'C:\Users\DELL\Desktop\codes\ml_codes\Ames_Housing_Data1.tsv', sep = '\t')
print(df.head())

df1 = df.drop_duplicates()
dup = df1.duplicated(['PID'])
# print(dup)

# find missing values
miss = df["Lot Frontage"].isnull().sum()
# miss1 = miss.head(20)
print(miss)

# for all colums 
miss = df.isnull().sum().sort_values(ascending = False)
miss1 = miss.head(20)
#print(miss)

median = df["Lot Frontage"].median()
df["Lot Frontage"].fillna(median,inplace = True)
#print(df['Lot Frontage'])
norm1 = df["Lot Frontage"].values #to convert pandas dataframe to numpy array
norm1 =norm1.reshape(-1,1)
#norm = sp.MinMaxScaler().fit_transform(norm1)
norm = sp.StandardScaler().fit_transform(norm1)
# minmax scaler needs 2d data input(almost all transforms require 2d data) If data were allowed to be 1D, it would be unclear whether that data represents multiple features of a single sample or a single feature across multiple samples.
#print(norm)
'''
sns.boxplot(x = df["Lot Frontage"])
plt.title("boxplot")
plt.show()

plt.scatter(x = df['Gr Liv Area'], y = df['SalePrice'])
plt.show()
'''
out1 = df.sort_values(by='Gr Liv Area',ascending=False)[:2]
drop_outliers = df.drop(df.index[[1499,2181]])
plt.scatter(x = drop_outliers['Gr Liv Area'], y = drop_outliers['SalePrice'])
plt.show()

