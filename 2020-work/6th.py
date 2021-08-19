def number():
    return float(a[:-2])

def Value():
    sum = len(a)
    return a[sum-2]

def ml_change():
    l = n/1000
    kl = n/1000000
    print(l,'l',kl,'kl')
    main()
    
def kl_change():
    ml = n*100000
    l = n*1000
    print(ml,'ml',l,'l')
    main()
    
def l_change():
    ml = n*1000
    kl = n/1000
    print(ml,'ml',kl,'kl')
    main()

def main():
    global a 
    a = input("값을 입력하세요: (나가기 : stop)")
    global Value 
    Value = Value()
    global n 
    n = number()
    
    if 'l' in a :
        if Value == 'm':
            ml_change()
        elif Value == 'k':
            kl_change()
        else:
            l_change()
            
    elif 'stop' in a:
        exit()
        
    else : print("잘못 입력하셨습니다.")
    

if __name__ == '__main__' :
    main()