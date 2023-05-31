fruits = ['apple', 'orange', 'banana', 'mango', 'watermelon']

from random import randint

def randomSentence(word) :
    randomIndex = randint(0, len(fruits)-1)
    return f'{fruits[randomIndex]} {word}'

with open('./text.txt') as file :
    para = file.read()
    wordlist = para.split()
    sentencelist = list(map(randomSentence, wordlist))

count = int(input('Paragraph Count : '))
for time in range(count) : 
    with open('./generator2.txt', 'a') as write_file :
        write_file.write(''.join(sentencelist) + '\n\n')