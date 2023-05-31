with open('./text.txt') as file :
    para = file.read()

count = int(input('Paragraph Count : '))
for time in range(count) : 
    with open('./generator.txt', 'a') as write_file :
        write_file.write(para + '\n\n')