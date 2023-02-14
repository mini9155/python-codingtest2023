import sys
input = sys.stdin.readline # 입력속도 개선을 위해 작성

N, M = tuple(map(int,input().split()))
numbers = list(map(int,input().split()))
sums =[0]
temp = 0
for i in numbers:
    temp = temp + i
    sums.append(temp)

for i in range(M):
    x, y = map(int, input().split())
    print(sums[y] - sums[x - 1])

