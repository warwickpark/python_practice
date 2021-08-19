import matplotlib.pyplot as plt

#A형 그래프
plt.bar(0.6,41,width=0.8,color='r')
plt.bar(1.4,32,width=0.8,color='b')
#B형 그래프
plt.bar(3.6,25,width=0.8,color='r')
plt.bar(4.4,31,width=0.8,color='b')
#O형 그래프
plt.bar(6.6,32,width=0.8,color='r')
plt.bar(7.4,36,width=0.8,color='b')
#AB형 그래프
plt.bar(9.6,12,width=0.8,color='r')
plt.bar(10.4,15,width=0.8,color='b')


#라벨
check=[1,4,7,10]
types=["A","B","O","AB"]
gender=["M","F"]
plt.xticks(check, types)

plt.xlabel('Blood type')
plt.ylabel('People')
plt.title('Blood type vs Sex')
plt.legend(gender)

plt.show()
