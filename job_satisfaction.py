import csv
from collections import defaultdict, Counter

with open('developer_survey_2019/survey_results_public.csv') as f:
    csv_reader = csv.DictReader(f)

    total = 0
    satisfaction_info = {}
    sat_mapper= {
    'Very dissatisfied' : 0,
    'Slightly dissatisfied' : 0.25,
    'Neither satisfied nor dissatisfied' : 0.5,
    'Slightly satisfied' : 0.75,
    'Very satisfied' : 1,
    }

    for lines in csv_reader:
        jobSats = lines['JobSat'] 
        carSats = lines['CareerSat']
        countries = lines['Country']
        genders = lines['Gender']
        trans = lines['Trans']
        total=0
        gender_type={'Man','Woman','Others'}
        for country in countries:
            if countries == 'NA':
                continue
            satisfaction_info.setdefault(countries, {
                'sat_m': 0,
                'sat_w': 0,                
                'sat_o': 0,
                'total_m': 0,
                'total_w': 0,
                'total_o': 0
            })
            if genders == 'Man':
                if (jobSats == 'NA') | (carSats == 'NA' ):
                    continue
                temp = sat_mapper[jobSats] + sat_mapper[carSats]
                if(temp > 1.0):
                    satisfaction_info[countries]['sat_m']+=1
                    satisfaction_info[countries]['total_m']+=1
                else:
                    satisfaction_info[countries]['total_m']+=1

            elif genders == 'Woman':
                if (jobSats == 'NA') | (carSats == 'NA' ):
                    continue
                temp = sat_mapper[jobSats] + sat_mapper[carSats]
                if(temp > 1.0):
                    satisfaction_info[countries]['sat_w']+=1
                    satisfaction_info[countries]['total_w']+=1
                else:
                    satisfaction_info[countries]['total_w']+=1
            else:
                if (jobSats == 'NA') | (carSats == 'NA' ):
                    continue
                temp = sat_mapper[jobSats] + sat_mapper[carSats]
                if(temp > 1.0):
                    satisfaction_info[countries]['sat_o']+=1
                    satisfaction_info[countries]['total_o']+=1
                else:
                    satisfaction_info[countries]['total_o']+=1   
                    
    for country,info in satisfaction_info.items():
        print(f'{country}:')
        print('\tMan :')
        if satisfaction_info[country]['total_m'] == 0:
            print(f'\tNo result!')
        else:
            score = round((satisfaction_info[country]['sat_m']/satisfaction_info[country]['total_m'])*100,1)   
            print(f'\t{score}%')
        print('\tWoman :')
        if satisfaction_info[country]['total_w'] == 0:
            print(f'\tNo result!')
        else:
            score = round((satisfaction_info[country]['sat_w']/satisfaction_info[country]['total_w'])*100,1)   
            print(f'\t{score}%')
        print('\tOthers :')
        if satisfaction_info[country]['total_o'] == 0:
            print(f'\tNo result!')
        else:
            score = round((satisfaction_info[country]['sat_o']/satisfaction_info[country]['total_o'])*100,1)   
            print(f'\t{score}%')
        print('\n')    
                
        
        
        
        
        
        
    
        