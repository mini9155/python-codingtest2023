# 백준 1541 - 잃어버린 괄호

answer = 0
A = list(map(str,input().split()))

def mysum(i):
    result = 0 # - 로 나눈 각 수식 문자열 합구하기 함수
    temp = str(i).split() # +기준으로 자름 ' 78 + 45 '
    
    for k in temp: # 
        result += int(k) # '78' 같은 문자열이므로 int로 변환
    
    return result

for s in range(len(A)):
    temp = mysum(A[s])

    if s == 0:
        answer += answer # 맨처음
    else:
        answer -= temp
    
print(answer)