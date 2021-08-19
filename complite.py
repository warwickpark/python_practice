import csv
import random

day_input = int(input(""))
# p = day_input*2-1
# q = p-1
# B = 0
# C = 0
num = 0
line_num = 0

wordlist = open('wordlist2.csv','r', newline='')
rdr = csv.reader(wordlist)
 
 # random_list에 뽑히면 뜻, 안 뽑히면 단어
random_list = random.sample(range(20),10)

for line in rdr:
    if(line_num in random_list):
        print(line[day_input*2-1])
    else:
        print(line[day_input*2-2])


    line_num += 1

#     if B == 10:
#          A = p
#     elif C == 10 :
#          A = q
#     else : A = random.randrange(q,p+1)

#     print(line[A])

#     if A%2 == 0:
#         B+=1
#     else : C+=1

 
wordlist.close()


