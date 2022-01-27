import os
import random

print("Random Tao")
print("Tao Te Ching by Lao Tzu")
print(" ")

path = '/Users/matthewwakeham/PycharmProjects/randomtao/taoteching/'
files = os.listdir(path)
if '.DS_Store' in files:
    files.remove('.DS_Store')
index = random.randrange(0, len(files))

file = path + '/' + files[index]
with open(file) as f:
    contents = f.read()
    print(contents)
