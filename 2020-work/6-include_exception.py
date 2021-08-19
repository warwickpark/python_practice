#문자열(단위) 분리
def number():
    try:
        return float(a[:-2])
    except:
        exception()

#문자열(숫자)분리
def Value():
    sum = len(a)
    return a[sum-2]

#단위변환
def ml_change():
    l = number()/1000
    kl = number()/1000000
    print(l,'l',kl,'kl')
    main()#다시 메인으로 돌아감

def kl_change():
    ml = number()*100000
    l = number()*1000
    print(ml,'ml',l,'l')
    main()#다시 메인으로 돌아감

def l_change():
    ml = number()*1000
    kl = number()/1000
    print(ml,'ml',kl,'kl')
    main()#다시 메인으로 돌아감

#단위 감지
def cheakvalue():
    if Value() == 'm':
        ml_change()
    elif Value() == 'k':
        kl_change()
    else:
        l_change()

#예외처리
def exception():
    print("예외가 발생했습니다! 제대로 입력해주세요")
    main()

#메인
def main():
    global a
    try:
        a = input("값을 입력하세요: (나가기 : stop)")
    except EOFError:
        print("Ctrl + D 그만 눌러요 EOF테스트 하지 말고!")
        main()
    except TypeError:
        print("stop 한번만 더 쳐주세요!")
        main()
    if a == 'stop':
        return
    elif 'l' in a: 
        cheakvalue()
    else:
        exception()

#실제로 실행되는 부분
main()