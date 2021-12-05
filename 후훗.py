def compare(a,b):
    if a == b:
        return True
    else:
        return False
def separation(a,b):
    return a/b
def main():
    A = input("첫번째 숫자")
    B = input("두번째 숫자")

    if len(A) != 3:
        main()
    elif len(B) != 3:
        main()
    else:
        zerozerozero = separation(int(A),100)
        zerozero = separation(int(B), 10)
    return int(zerozerozero),int(zerozero)

print(main())





