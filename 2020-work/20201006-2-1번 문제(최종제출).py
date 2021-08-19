import matplotlib.pyplot as plt

types=["A","B","O","AB"]#가로선에 쓸 내용들 지정
plt.xticks((range(1,5)), types)
#                        ↳가로선에 쓸 내용 
#            ↳1부터 5까지 숫자 생성
#           ↳가로선의 x축 위치 지정   
#   ↳가로선 설정
plt.xlabel('Blood type')#x축 라벨
plt.ylabel('People')#y축 라벨
plt.title('Distribution of lood types')#제목
plt.bar(1,73,width=0.4,color='k')
plt.bar(2,86,width=0.4,color='r')
plt.bar(3,68,width=0.4,color='b')
plt.bar(4,27,width=0.4,color='g')
#                      ↳막대의 색 지정
#            ↳막대의 두께 지정
#         ↳y축 위치(자료의 값)
#       ↳x축 위치
#   ↳막대그래프 생성
plt.show()#그래프 출력

"""
윈래는
plt.bar(x축 위치가 있는 리스트,자료의 값이 들어있는 리스트,(기타 설정))
으로 구현해야하나....
그렇게 하면 색 지정을 못해서.....
하나하나 위치 지정하고 색 바꿈....
"""
