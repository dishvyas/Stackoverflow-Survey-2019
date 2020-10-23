import csv
from collections import defaultdict, Counter

#CompTotal Countries
with open('developer_survey_2019/survey_results_public.csv') as f:
    csv_reader = csv.DictReader(f)
    salary_info = {}
    for line in csv_reader:
        countries = line['Country']
        salaries = line['CompTotal']
        for country in countries:
            if countries == 'NA':
                continue
            if salaries == 'NA':
                continue
            salary_info.setdefault(countries, {
                'count': 0,
                'salary': 0
            })
            salary_info[countries]['count']+=1
            salary_info[countries]['salary']+=float(salaries)  
    
    print('Average Salaries:')
    for country, info in salary_info.items():
        count = round((info['salary']/info['count']),0)
        
        print(f'\t{country}: {count}')