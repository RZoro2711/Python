# files = open('./text.txt')
# for file in files :
#     print(file)

# files.seek(0)
# linelist = files.readlines()
# print(linelist)

# files.seek(50)
# para = files.read(100)
# print(para)
# files.close()


with open('./text.txt') as file :
    for line in file :
        print(line)