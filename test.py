def calc(v1,v2,op) :
    result = 0
    print(v1,v2,op)

    if op == '-' :
        result = v1 - v2
        print("work!!")   
    elif op == '*' :
        result = v1 * v2
        print("work!!")   
    elif op == '/' :
        result = v1 / v2
        print("work!!")   
    elif op == '**' :
        result = v1 ** v2
        print("work!!")   
    else:
        result = v1 + v2
        print("work!!")   
    print(result,type(result))     
    return result

res = 0
var1, var2, oper = 0, 0, ""

var1 = int(input("\n첫 번째 수를 입력하세요 : "))
print(type(var1),var1)
oper = input("계산을 입력하세요 (+, -, *, /, **) : ")
print(type(oper),oper)
var2 = int(input("두 번째 수를 입력하세요 : "))
print(type(var2),var2)
if oper == '/' and var2 == 0:
    print("0으로는 나누면 안 됩니다. ㅠㅠ")
else :
    rec = calc(var1, var2, oper)
    print("## 계산기 : ", var1, oper, var2, "=", rec)
