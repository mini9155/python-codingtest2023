checklist = [0] * 4 # acgt 유전자값
mylist = [0] * 4 # 부분 문자열의 ACGT 갯수
checksecret = 0

# 함수
def myadd(c): # 새로 들어온 문자를 처리
    global checksecret, mylist, checklist
    if c == 'A':
        mylist[0] += 1
        if mylist[0] == checklist[0]:
            checksecret += 1
    elif c == 'C':
        mylist[1] += 1
        if mylist[1] == checklist[1]:
            checksecret +=1
    elif c == 'G':
        mylist[2] += 1 # mylist 2번에 1을 더해라
        if mylist[2] == checklist[2]:
            checksecret +=1
    elif c == 'T':
        mylist[3] += 1
        if mylist[3] == checklist[3]:
            checksecret +=1

def myremove(c): # 새로 들어온 문자를 처리
    global checksecret, mylist, checklist
    if c == 'A':
        if mylist[0] == checklist[0]:
            checksecret -= 1
        mylist[0] -= 1
    elif c == 'C':
        if mylist[1] == checklist[1]:
            checksecret -=1
        mylist[1] -= 1
    elif c == 'G':
        if mylist[2] == checklist[2]:
            checksecret -=1
        mylist[2] -= 1
    elif c == 'T':
        if mylist[3] == checklist[3]:
            checksecret -=1
        mylist[3] -= 1

S, P = map(int, input().split())
Result = 0
A = list(input())
checklist = list(map(int,input().split()))

for i in range(4):
    if checklist[i] == 0: # checklist[i]가 0이면
        checksecret += 1 # checksecret에 1을 더해라
for i in range(P): #부분문자열 갯수 만큼
    myadd(A[i])

if checksecret == 4:
    Result += 1
for i in range(P,S):
    j = i - P
    myadd(A[i]) # 이번 슬라이드에서
    myremove(A[j]) # 이전 슬라이드서 처리한 값을 제거
    if checksecret == 4:
        Result += 1

print(Result)