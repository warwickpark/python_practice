import csv
import pandas as pd
 
wordlist = open('wordlist2.csv','r', newline='')
rdr = csv.reader(wordlist)

count = 0
word = []
mean = []

print(type(rdr))
print(rdr)

for line in rdr:
    word = line[0]
    mean = line[1]
    count = count + 1

print(type(word))
print(type(mean))

print(word)

#for i in word:
#    print(i)
#for j in mean:
#    print(j)

wordlist.close()