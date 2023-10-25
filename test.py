import pandas as pd
data = (r'C:\Users\ADMIN\Desktop\pandasApp\title-akas-us-only.csv')
df = pd.read_csv(data)
df = df[df['region'] == 'US']
print(df)