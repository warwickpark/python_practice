#문자열 분리
def number():
    return float(a[:-2])
def Value():
    sum = len(a)
    return a[sum-2]

#단위변환
def ml_change():
    l = n/1000
    kl = n/1000000
    print(l,'l',kl,'kl')
def kl_change():
    ml = n*100000
    l = n*1000
    print(ml,'ml',l,'l')
def l_change():
    ml = n*1000
    kl = n/1000
    print(ml,'ml',kl,'kl')

#실행코드
a = input()
Value = Value()
n = number()

#분류
if Value == 'm':
    ml_change()
elif Value == 'k':
    kl_change()
else:
    l_change()
