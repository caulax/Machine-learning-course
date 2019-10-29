import pandas as pd

df = pd.read_csv('adult.data.csv')

# 1
print(len(df[df.sex == "Male"]))
print(len(df[df.sex == "Female"]))

# 2
print(df[df.sex == "Female"]["age"].mean())

# 3
print(len(df[df["native-country"] == "Germany"]))

# 4-5
print("Avg: ", df[df["salary"] == "<=50K"]["age"].mean())
print("Std", df[df["salary"] == "<=50K"]["age"].std())

# 6
salary_over_50 = df[df.salary == ">50K"].copy()

print("Salary over 50 and have higher education: ", len(salary_over_50[salary_over_50.education.isin(["Bachelors", "Prof-school", "Assoc-acdm", "Assoc-voc", "Masters", "Doctorate"])]))

print("Salary over 50 and do not have higher education: ", len(salary_over_50[~salary_over_50.education.isin(["Bachelors", "Prof-school", "Assoc-acdm", "Assoc-voc", "Masters", "Doctorate"])]))

# 7
statistics_by_age_race_sex = df[["age", "race", "sex"]].groupby(["race", "sex"]).describe().reset_index()
print(statistics_by_age_race_sex)
print(statistics_by_age_race_sex[(statistics_by_age_race_sex.race == "Amer-Indian-Eskimo") & (statistics_by_age_race_sex.sex == "Male")].max)

# 8
salary_over_50_and_male = df[(df.salary == ">50K") & (df.sex == "Male")]

print("Married and over 50k: ", len(salary_over_50_and_male["marital-status"].isin(["Married", "Married-civ-spouse", "Married-spouse-absent", "Married-AF-spouse"])))
print("Not married and over 50k: ", len(salary_over_50_and_male[~salary_over_50_and_male["marital-status"].isin(["Married", "Married-civ-spouse", "Married-spouse-absent", "Married-AF-spouse"])]))

# 9
max_hours_per_week = df["hours-per-week"].max()
print("Max hours working:", max_hours_per_week)
persons_max_work = len(df[df["hours-per-week"] == max_hours_per_week])

print("Persons who worked max hours per week:", persons_max_work)

persons_max_hours_over_50 = len(df[(df["hours-per-week"] == max_hours_per_week) & (df.salary == ">50K")])

print("Persons who worked max hours per week and earned more 50k:", persons_max_hours_over_50)
print("Percent:", (persons_max_hours_over_50 / persons_max_work) * 100)

# 10
print("Avg by country and earn more 50:", df[df.salary == ">50K"].groupby("native-country")["hours-per-week"].mean())
print("Avg by country and earn less 50:", df[df.salary == "<=50K"].groupby("native-country")["hours-per-week"].mean())
