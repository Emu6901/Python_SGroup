import numpy as np
import pandas as pd

# 1. Read Salaries.csv as a dataframe called sal

sal = pd.read_csv('Salaries.csv')

# 2. Check the head of the DataFrame.

print(sal.head())

# 3. Use the .info() method to find out how many entries there are.

print(sal.info())

# 4. What is the average BasePay ?

print('Average BasePay: ',sal['BasePay'].mean())

# 5. What is the highest amount of OvertimePay in the dataset ?

print('Highest amount of OvertimePay: ',sal['OvertimePay'].max())

# 6. What is the job title of JOSEPH DRISCOLL ? Note: Use all caps, otherwise you may get an answer that doesn't 
# match up (there is also a lowercase Joseph Driscoll).

sal_JOSEPH_DRISCOLL = sal[sal['EmployeeName'] == 'JOSEPH DRISCOLL']
print('Job title of JOSEPH DRISCOLL: ',sal_JOSEPH_DRISCOLL['JobTitle'])

# 7. How much does JOSEPH DRISCOLL make (including benefits)?

print('TotalPayBenefits of JOSEPH DRISCOLL: ', sal_JOSEPH_DRISCOLL['TotalPayBenefits'])

# 8. What is the name of highest paid person (including benefits)?

Highest_paid_person = sal[sal['TotalPayBenefits'] == sal['TotalPayBenefits'].max()]
print('Name of highest paid person : \n', Highest_paid_person[['Id', 'EmployeeName', 'TotalPayBenefits']])

# 9. What is the name of lowest paid person (including benefits)? Do you notice something strange about how much he
# or she is paid?

Lowest_paid_person = sal[sal['TotalPayBenefits'] == sal['TotalPayBenefits'].min()]
print('Name of lowest paid person: \n', Lowest_paid_person[['Id', 'EmployeeName', 'TotalPayBenefits']])

# I have no idea why his/her TotalPayBenefits < 0.

# 10. What was the average (mean) BasePay of all employees per year? (2011-2014) ?

BasePay_per_years = sal.groupby('Year').mean()['BasePay']
print('The average (mean) BasePay of all employees per year: \n', BasePay_per_years)

# 11. How many unique job titles are there?

sal_job_title = sal['JobTitle']
print('Number of unique job titles: ', sal_job_title.nunique())

# 12. What are the top 5 most common jobs?

most_common_job = sal_job_title.value_counts()
print('Top 5 most common jobs: \n', most_common_job.head())

# 13. How many Job Titles were represented by only one person in 2013? (e.g. Job Titles with only one occurence in
# 2013?)

sal_job_title_in_2013_by_one_person = sum(sal[sal['Year'] == 2013]['JobTitle'].value_counts() == 1)
print('Number of Job Titles were represented by only one person in 2013: ', sal_job_title_in_2013_by_one_person)

# 14. How many people have the word Chief in their job title? (This is pretty tricky)

list_of_job = sal_job_title.tolist()
cnt = 0
for i in list_of_job:
    if 'chief' in i.lower():
        cnt += 1
print('Number of people have the word Chief in their job title: ', cnt)

# 15. Bonus: Is there a correlation between length of the Job Title string and Salary?

lenght_of_job_title = []
for i in list_of_job:
    lenght_of_job_title.append(len(i))
sal['Lenght Of Job Title'] = lenght_of_job_title
print(sal[['Lenght Of Job Title', 'TotalPayBenefits']].corr())
