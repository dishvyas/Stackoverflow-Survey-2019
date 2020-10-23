import csv
from collections import defaultdict, Counter

def isinteger(a):
    try:
        int(a)
        return True
    except ValueError:
        return False

with open('developer_survey_2019/survey_results_public.csv') as f:
    csv_reader = csv.DictReader(f)

    dev_type_info = {}
    ageTotal = 0
    total = 0
    python_info = {}
    for line in csv_reader:
        dev_types = line['Age1stCode']
        # Discard if value is NA or NAN
        if(isinteger(dev_types)==True) :
            ageTotal+=int(dev_types)
            total+=1
    print("Avg age of developers when they wrote first line of code :")
    print(int(ageTotal/total))
    
    





