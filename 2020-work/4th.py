def inp():
    print("ax+by+c = 0\n dx+ey+f = 0 의 값을 입력하시오.")

def solve_lin_eqns(a,b,c,d,e,f):
    sum = ((-c)*e) + (b*f)
    num = (a*e) - (b*d)
    x = sum / num
    sum = ((-a)*f) + (d*c)
    num = (a*e) - (b*d)
    y = sum / num
    print("x = ",x,"y = ",y)
    return x, y


if __name__ == '__main__':
    inp()
    print("a의 값을 입력하시오.")
    a = int(input())
    print("b의 값을 입력하시오.")
    b = int(input())
    print("c의 값을 입력하시오.")
    c = int(input())
    print("d의 값을 입력하시오.")
    d = int(input())
    print("e의 값을 입력하시오.")
    e = int(input())
    print("f의 값을 입력하시오.")
    f = int(input())
    solve_lin_eqns(a,b,c,d,e,f)