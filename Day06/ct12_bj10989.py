# 백준 10989 - 수 정렬하기

import sys
input = sys.stdin.readline

N =int(input())
count  = [0] * 10001

for i in range(N): # 천만번 데이터를 넣는다
    count[int(input())] += 1 # count 배열 순서에 1을 넣는다

for i in range(10001): # i가 10001이 될 때까지 돈다
    if count[i] != 0: # 만약 count[i]가 0이 아니라면
        print(i)
        # for _ in range(count[i]):
        #     print(i)