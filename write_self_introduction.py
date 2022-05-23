import json
from collections import Counter
new_dict = Counter()
new_dict['name'] = 'Sota Sakai'
new_dict['birth_day'] = '2000/10/26'
new_dict['school'] = {
    'highschool': 'Kobe City College of Technology',
    'university': 'Osaka'}
new_dict['hobby'] = 'book'
with open('data/self.json', 'w')as f:
    json.dump(new_dict, f, indent=2, ensure_ascii=False)
