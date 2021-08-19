def inp():
    print("ax+by+c = 0\n dx+ey+f = 0 의 값을 입력하시오.")

   
def solve_lin_eqns(a,b,c,d,e,f):
    sum = ((-c)*e) + (b*f)
    num = (a*e) - (b*d)
    x = sum / num
    sum = ((-a)*f) + (d*c)
    num = (a*e) - (b*d)
    y = sum / num
    print(x ,y)
  
if __name__ == '__main__':
    inp()
    print("a")
    a = int(input())
    print("b")
    b = int(input())
    print("c")
    c = int(input())
    print("d")
    d = int(input())
    print("e")
    e = int(input())
    print("f")
    f = int(input())
    solve_lin_eqns(a,b,c,d,e,f)