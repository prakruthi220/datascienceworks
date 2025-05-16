import pandas as pd
import numpy as np

data = pd.read_csv(r'C:\Users\DELL\Desktop\ml_codes\Placement_Data_Full_Class.csv')
# print(data.columns)

# calculate interquartile range
q25,q50,q75 = np.percentile(data['12th %'],[25,50,75])
iqr = q75-q25

# calculate the min/max  limits to be considered an outlier
min1 = q25 - 1.5 * (iqr)
max1 = q75 + 1.5 * (iqr)
print(min1,q25,q50,q75,max1)

# identify the points
for x in data['12th %']:
    if x > max1 or x < min1:
       print(x) 