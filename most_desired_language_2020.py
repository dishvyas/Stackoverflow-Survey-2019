import csv
from collections import defaultdict, Counter
import operator

lang_info={"NA": 0, "Assembly": 0, "Bash/Shell/PowerShell": 0, "C": 0, "C++": 0, "C#": 0, "Clojure": 0, "Dart": 0, "Elixir": 0, "Erlang": 0, "F#": 0, "Go": 0, "HTML/CSS": 0, "Java": 0, "JavaScript": 0, "Kotlin": 0, "Objective-C": 0, "PHP": 0, "Python": 0, "R": 0, "Ruby": 0, "Rust": 0, "Scala": 0, "SQL": 0, "Swift": 0, "TypeScript": 0, "VBA": 0, "WebAssembly": 0, "Other(s):": 0}

def highest_freq(lst):
   for sublist in lst:
       for el in sublist:
           lang_info[sublist]+=1 
   return max(lang_info.items(), key=operator.itemgetter(1))[0]

with open('developer_survey_2019/survey_results_public.csv') as f:
    csv_reader = csv.DictReader(f)

    total_count=0
    for lines in csv_reader:
        languages = lines['LanguageDesireNextYear'].split(';')
        
        most_desired_langugae=highest_freq(languages)
    # Uncomment below line to see count of each language from the survey
    # print(lang_info)
    print('Most Desired Language of 2020 is:')
    print(f'\t{most_desired_langugae}')