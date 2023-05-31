# with open('./about.txt', 'w') as file :
#     file.write('I"m Khunn Satt Ko Ko')
# with open('./about.txt', 'a') as file :
#     file.write('\n I"m 21 years old.')
# with open('./about.txt', 'a') as file :
#     file.write('\n I"m a junior web developer.')

lists = ['I"m Khunn Satt Ko Ko', '\n I"m 21 years old.']
with open('./about.txt', 'w') as file :
    file.writelines(lists)