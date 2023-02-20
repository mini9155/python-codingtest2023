# 최소공배수
a,b = map(int,input().split())
A = a
B = b

if A == B:
    pass
else:
    i = 0
    while A != B:
        i += 1
        if A > B:
            B = b * i
            if B > A:
                i = 1
        elif A < B:
            A = a * i
            if A > B:
                i = 1
    if A == B:
        print(A)