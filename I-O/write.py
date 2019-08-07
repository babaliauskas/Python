with open('I-O/file.txt', 'w') as file:
    file.write('asdasdasdasd\n')
    file.write('adfasdf')


##########################

with open('I-O/file.txt') as readFile:
    readFile.read()


##################

with open('I-O/file.txt', 'r+') as readFile:
    readFile.write('asdfasdfasdf \n')


##################

with open('I-O/file.txt', 'a') as readFile:
    readFile.write('asdfasdfasdf \n')
