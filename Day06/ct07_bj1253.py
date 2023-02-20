import sys
input = sys.stdin.readline

N =int(input())
Result = 0
count = 0
A = list(map(int,input().split())) # 한줄에 입력 다 받을 떄
A.sort() # 전체 정렬, 순차적으로
for k in range(N):
    find = A[k]
    i = 0; j = N-1 #i는 리스트 첫번째, j는 리스트 마지막번째 위치
    while i < j: # 두 인덱스가 결국 만나면 while문을 종료
        if A[i] + A[j] == find:
            if i != k and j != k: #i,j는 k랑 같은 위치가 되면 안됨!!
                count += 1
                break
            elif i == k: i += 1
            elif j == k: j -= 1
        elif A[i] + A[j] <find: # i를 증가시켜야 합의 수가 커진다
            i += 1
        elif A[i] + A[j] >find: # i를 증가시켜야 합의 수가 작아짐
            j -= 1

print(count)