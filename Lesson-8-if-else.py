age = int(input('Enter Your Age : '))
if age < 18 :
    print('Your are young.')
elif age > 18 and age < 30 :
    print('Your are normal age.')
else :
    print('You are old.')

q = input("Are you tired? 'y/n' : ")
if q=='y' or q=='yes' or q=='Yes' : 
    print("I'm tired.")
elif q=='n' or q=='no' or q=='No' :
    print('I"m not tired.')
else :
    print('Enter y/n')