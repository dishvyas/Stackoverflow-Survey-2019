import csv
from collections import defaultdict, Counter

with open('developer_survey_2019/survey_results_public.csv') as f:
    csv_reader = csv.DictReader(f)

    total = 0
    python_info = {}
    
    for lines in csv_reader:
        languages = lines['LanguageWorkedWith'].split(';')
        countries = lines['Country'] 
        for country in countries:
            if countries == 'NA':
                continue
            python_info.setdefault(countries, {
                'total': 0,
                'lang': 0
            })
            python_info[countries]['total']+=1
            for language in languages:
                if language == 'Python' : 
                    python_info[countries]['lang']+=1  
    print("% of developers who know python in each country :")
    for country, info in python_info.items():
        count = round((info['lang']/info['total'])*100,1)
        
        print(f'\t{country}: {count}%')