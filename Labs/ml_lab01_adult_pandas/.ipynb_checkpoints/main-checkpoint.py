import pandas as pd


df = pd.read_csv('adult.data.csv')

# 1
# print(len(df[df.sex == "Male"]))
# print(len(df[df.sex == "Female"]))

print(df[df.sex == "Female"]["age"].mean())
