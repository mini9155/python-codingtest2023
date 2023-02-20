from collections import deque
N, L = map(int, input().split()) # map이란 함수에 int로 받는다
mydeque = deque()
now = list(map(int,input().split()))

for i in range(N):
    while mydeque and mydeque[-1][0] > now[i]: # 마지막 위치에서부터 현재 값보다 큰 값은 덱에서 제거  
        mydeque.pop() # 데이터를 삭제
    mydeque.append((now[i],i)) # mydeque에 i번이랑 i를 넣는다
    if mydeque[0][1] <= i - L: # 범위를 벗어난 값도 덱에서 제거
        mydeque.popleft() # 왼쪽 값을 제거
    print(mydeque[0][0], end=' ')  #0번쨰에 있는 0번쨰 값을 출력, 무조건 최소값(min과 동일)