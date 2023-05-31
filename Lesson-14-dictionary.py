person = {
    'name' : 'Khunn Satt Ko Ko',
    'age' : 21,
}
print(person['name'])
print(person['age'])

person['gender'] = 'Male'
print(person)

if 'name' in person :
    print('Success')
else :
    print('Fail')

print(list(person.keys()))
print(list(person.values()))