import matplotlib.pyplot as plt

#1
plt.bar(0.25,41,width=0.4,color='k')
plt.bar(0.75,25,width=0.4,color='r')
plt.bar(1.25,32,width=0.4,color='b')
plt.bar(1.75,12,width=0.4,color='g')
#2
plt.bar(3.25,32,width=0.4,color='k')
plt.bar(3.75,31,width=0.4,color='r')
plt.bar(4.25,36,width=0.4,color='b')
plt.bar(4.75,15,width=0.4,color='g')


#라벨
check=[1,4]
types=["M","F"]
types2=['A','B','O','AB']
plt.xticks(check, types)
plt.xlabel('Sex')
plt.ylabel('People')
plt.title('Blood type vs Sex')
plt.legend(types2)
#범례 설정
plt.show()


"""
                                            
     (-0.75)     (-0.25)        (+0.25)       (+0.75)               
   0.3 0.3     0.3 0.3     0.3 0.3     0.3 0.3                                              
           0.4         0.4         0.4                     
                        X                         
                                                  
                                                  
---------x-----------------------------x----------



"""