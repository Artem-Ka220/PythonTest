import pprint
people = {'ford' : {'Name' : 'Ford Perfect',
                    'Gender' : 'Male',
                    'Occupation' : 'Reasearcher',
                    'Home Planet' : 'Betelgeuse Seven'},
          'sokolov' : {'Name' : 'Artem Sokolov',
                    'Gender' : 'Male',
                    'Occupation' : 'Programmer',
                    'Home Planet' : 'Earth'}}
print(people)
print()
for i in people:
    print(i)
    for k, j in people[i].items():
        print(k, ':', j)

pprint.pprint(people)
