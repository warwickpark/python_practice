def prt():
   print('변환하고자 하는 값을 입력하세요 :  (나가기 : stop)')

def ml_change(a):
   p = len(a)
   q = p-2
   num = a[0:q]
   l = int(num) / 1000
   kl = int(num) / 1000000
   print(l,"l", kl,"kl")
   main()

def l_change(a):
   p = len(a)
   q = p-1
   num = a[0:q]
   ml = int(num)*1000
   kl = int(num)/1000
   print(ml,"ml", kl,"kl")
   main()
   
def kl_change(a):
   p = len(a)
   q = p-2
   num = a[0:q]
   ml = int(num)*1000000
   l = int(num)*1000
   print(ml,"ml", l,"l")
   main()

def main():
      prt()
      a=input()
      if 'l' in a:
         if 'm' in a:
            ml_change(a)
         elif 'k' in a:
            kl_change(a)
         else :
            l_change(a)
      elif 'stop' in a:
          print("종료")
          exit()
      else :
          print("잘못된 형태입니다.")
          main()

if __name__ == '__main__':
    main()