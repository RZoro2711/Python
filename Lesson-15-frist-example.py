person = {}
while True :
    name = input('Name : ')
    age = input('Age : ')
    person[name] = age
    another = input('Add more ? y/n : ')
    if another == 'y' or another == 'yes' or another == 'Yes' :
        continue
    else :
        break

# for (key,value) in person.items() :
#     print(f'{key} is {value} years old.')

ages = list(person.values())
for age in set(ages) :
    count = ages.count(age)
    print(f'{age} years old - {count}' )