import csv
 
wordlist_1 = open('wordlist_1.csv','r', newline='')
wordlist_2 = open('wordlist_2.csv','r', newline='')
wordlist_3 = open('wordlist_3.csv','r', newline='')
wordlist_4 = open('wordlist_4.csv','r', newline='')
wordlist_5 = open('wordlist_5.csv','r', newline='')

def selectfile():
    a = input("불러올 파일 이름을 입력하세요")


rdr = csv.reader(selectlist)
 
for line in rdr:
    print(line[1])
 
wordlist_1.close()
wordlist_2.close()
wordlist_3.close()
wordlist_4.close()
wordlist_5.close()