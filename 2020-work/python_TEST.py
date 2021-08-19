import os, math, fractions
import sympy as sym
import matplotlib.pyplot as plt
from fractions import Fraction
os.system('cls')

print("1-1번 문제")
print("\n소스코드")
print("print(\"몫\",17589391/231)\nprint(\"나머지\",17589391%231)")
print("\n결과")
print("\n몫",17589391//231)
print("나머지",17589391%231)
os.system("pause")
os.system('cls')

print("1-2번 문제")
print("\n소스코드")
print("import math\nprint(\"sin(35°)\", math.sin(35))")
print("\n결과")
print("sin(35°)", math.sin(35))
os.system("pause")
os.system('cls')

print("1-3번 문제")
print("\n소스코드")
print("import sympy as sym\na,b=sym.symbols('a,b')\nexpr=a*a-b+a*b+b/a\nsym.pprint(expr)\nAns=expr.subs({a:1+2j,b:3-4j})\nprint(sym.simplify(Ans))")
print("\n결과")
a,b=sym.symbols('a,b')
expr=a*a-b+a*b+b/a
sym.pprint(expr)
Ans=expr.subs({a:1+2j,b:3-4j})
print("답",sym.simplify(Ans))
os.system("pause")
os.system('cls')

print("1-4번 문제")
print("\n소스코드")
print("import sympy as sym\na=115/731231\nb=12314/131347\nsym.pprint(sym.Rational(a+b))")
print("\n결과")
a=115/731231
b=12314/131347
sym.pprint(sym.Rational(a+b))
os.system("pause")
os.system('cls')

print("1-5번 문제")
print("\n소스코드")
print("for i in range(10,100):\n   a+=(51*i)+3         \n   print(a)")
print("\n결과")
a=0
for i in range(10,100):
    a+=(51*i)+3         
print(a)
os.system("pause")
os.system('cls')


print("2번 문제")
print("\n소스코드")
print("")
print("\n결과")

os.system("pause")
os.system('cls')


print("3번 문제")
print("\n소스코드")
print("")
print("\n결과")

os.system("pause")
os.system('cls')


print("4번 문제")
print("\n소스코드")
print("")
print("\n결과")

os.system("pause")
os.system('cls')



