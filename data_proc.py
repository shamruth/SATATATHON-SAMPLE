import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer
data=pd.read_csv('data.csv')
print(data)

missing_values = ["", "NA", "N/A", "n/a", "na", "--"]
df = pd.read_csv('data.csv', na_values=missing_values)
print(df)
#imputing missing values
numeric_col=df.select_dtypes(include=np.number).columns
string_col=df.select_dtypes(include='object').columns
print(numeric_col)
print(string_col)

numeric_imputer=SimpleImputer(strategy='median')
df[numeric_col]=numeric_imputer.fit_transform(df[numeric_col])
print(df)
#calculating interquartile range for identifying outliers
Q1 = df['age'].quantile(0.25)
Q3 = df['age'].quantile(0.75)
IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR
#identifing the outliers
outliers = df[(df['age'] < lower_bound) | (df['age'] > upper_bound)]
print("\nOutliers Found:")
print(outliers)
#capping the outliers
df['age'] = np.where(
    df['age'] > upper_bound,
    upper_bound,
    df['age']
)
df['age'] = np.where(
    df['age'] < lower_bound,
    lower_bound,
    df['age']
)
print(df)
#validating the  age and educational qualification
rows_mask = (df['age'] < 18) & (df['education'] == 'Graduate')
print("\nViolating rows found:")
print(df[rows_mask])
#applying the correction by locating the existing invakidated age and manipulating the values
df.loc[rows_mask, 'education'] = 'High School'
print(df)