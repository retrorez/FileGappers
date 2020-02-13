#! python3

# Fill in the Gaps - Searches a folder for files that are numbered and checks
# for gaps in the numbering. If found, it corrects the gap.

import os, re

# create list for found files with numbers
trimmed = []
withNumbers = []

counter = 0

# change to gappers directory
os.chdir('C:\\code\\python\\gappers')
print(os.getcwd())

# scan directory for a sequence of numbers?
print(os.listdir())

sequenceRegex = re.compile(r'[0-9]+$') # create regex that searches for numbers at the end

for file in os.listdir():
    filename = str(file)[:-4]
    trimmed.append(filename)
    

print(trimmed)

for file in trimmed:
    try:
        if sequenceRegex.search(file).group():
            print('Got one: ' + file)
            withNumbers.append(sequenceRegex.search(file).group())
            counter = counter + 1
            lastFile = sequenceRegex.search(file).group()
    except Exception as err:
        continue
        
print(withNumbers)

# if found, make sure they are numbered properly

print('Number of last File: ' + lastFile)
print('length of numbering:' + str(len(lastFile)))
print('Number of files in set: ' + str(counter))
if int(lastFile) != counter:
    print('Incorrect Numbering!')
else:
    print('Numbering appears correct!')
    


# if not, correct the order
