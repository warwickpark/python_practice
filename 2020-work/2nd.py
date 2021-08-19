#문자열 분리
def number():
    return float(a[:-2])
def Value():
    sum = len(a)
    return a[sum-2]

#단위변환
def ml_change():
    l = number()/1000
    kl = number()/1000000
    print(l,'l',kl,'kl')
def kl_change():
    ml = number()*100000
    l = number()*1000
    print(ml,'ml',l,'l')
def l_change():
    ml = number()*1000
    kl = number()/1000
    print(ml,'ml',kl,'kl')

#실행코드
a = input()
if Value() == 'm':
    ml_change()
elif Value() == 'k':
    kl_change()
else:
    l_change()
