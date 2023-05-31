from urllib.request import urlretrieve
link = input('Input Download Link : ')
filename = input('File Name : ')
urlretrieve(link, 'image/' + filename + '.jpg')