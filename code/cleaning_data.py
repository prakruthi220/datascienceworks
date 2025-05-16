import pandas as pd
import seaborn as sns
import matplotlib as plot
import numpy as np

data = pd.read_csv(r'C:\Users\DELL\Desktop\ml_codes\Ames_Housing_Data1.tsv', sep='\t')
#print((data.columns))
#print(data["SalePrice"].describe())
#print(data["Sale Condition"].value_counts)

corr1 = data.select_dtypes(include = ['float64', 'int64'])
corr2 = corr1.corr()['SalePrice'][:-1]
top = corr2[abs(corr2) > 0.5].sort_values(ascending = False)
#print(top)
#print(corr1)
print("skewness: %f",data["SalePrice"].skew())
log_transformed = np.log(data["SalePrice"])
print("skewness: %f",log_transformed.skew())

