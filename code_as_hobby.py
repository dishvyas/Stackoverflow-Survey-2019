import csv
from collections import defaultdict, Counter

with open('developer_survey_2019/survey_results_public.csv') as f:
    csv_reader = csv.DictReader(f)

    total = 0
    hobby_info = {}
    list_of_country = {}
    for lines in csv_reader:
        countries = lines['Country']
        genders = lines['Gender'] 
        hobbies = lines['Hobbyist']
        gender_type={'Man','Woman','Others'}
        for country in countries:
            if countries == 'NA':
                continue
            # if countries not in list_of_country:
            #     list_of_country.add(countries)
            hobby_info.setdefault(countries, {
                'as_hobbyM': 0,
                'totalM': 0,
                'as_hobbyW': 0,
                'totalW': 0,
                'as_hobbyO': 0,
                'totalO': 0
            })
            if genders == 'Man':
                if hobbies == 'Yes':
                    hobby_info[countries]['as_hobbyM']+=1
                    hobby_info[countries]['totalM']+=1
                else:
                    hobby_info[countries]['totalM']+=1
            elif genders == 'Woman':
                if hobbies == 'Yes':
                    hobby_info[countries]['as_hobbyW']+=1
                    hobby_info[countries]['totalW']+=1
                else:
                    hobby_info[countries]['totalW']+=1
            else:
                if hobbies == 'Yes':
                    hobby_info[countries]['as_hobbyO']+=1
                    hobby_info[countries]['totalO']+=1
                else:
                    hobby_info[countries]['totalO']+=1
            
    print(len(hobby_info))
    for country,info in hobby_info.items():
        print(f'{country}:') 
        print('\tMan :')
        if hobby_info[country]['totalM'] == 0:
            print(f'\tNo result!')
        else:
            score = round((hobby_info[country]['as_hobbyM']/hobby_info[country]['totalM'])*100,1)   
            print(f'\t{score}%')
        print('\tWoman :')
        if hobby_info[country]['totalW'] == 0:
            print(f'\tNo result!')
        else:
            score = round((hobby_info[country]['as_hobbyW']/hobby_info[country]['totalW'])*100,1)   
            print(f'\t{score}%')
        print('\tOthers :')
        if hobby_info[country]['totalO'] == 0:
            print(f'\tNo result!')
        else:
            score = round((hobby_info[country]['as_hobbyO']/hobby_info[country]['totalO'])*100,1)   
            print(f'\t{score}%')
        print('\n')