# python-codingtest2023
파이썬 코딩테스트 리포지토리



# 1일차
1. 코딩테스트 소개
2. 코딩테스트 학습
    - 자료구조
    - ....


# 2일차
! 파이썬 파일명에는 _만 사용할 것!!
1. 코딩테스트 학습
    - 구간합2
    - 자료구조 다시
        - 연결 리스트
        - 스택
        - 큐
    - 파이썬 미리 구현된 스택, 큐, 기타 자료구조 확인!

# 3일차
- 자료구조
    - 큐
    - 이진트리
        - 삭제는 연결리스트 삭제와 유사
    - 그래프


# 4일차
1. 코딩테스트 학습
    - 재귀호출
    - 그래프 - DFS
    - 정렬소개

# 5일차
1. 코딩테스트 학습
    - 자료구조 / 알고리즘
        - 정렬
        - 검색
        - 다이나믹 프로그래밍

# 6일차
1. 코딩테스트 학습
    - 자료구조
        - 덱
    - 코딩테스트 알고리즘
        - 투 포인터
        - 슬라이딩 윈도우
        - 정렬
```python
# 백준 11003
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
```

# 7일차
1. 코딩테스트 학습
    - 자료구조
        - [x]그래프
        - [x]prioriyQueue(우선순위 큐)
        - [x] heapq(힙큐)
    - 알고리즘
        - [x] 탐색 DFS/BFS/이진탐색
        - [] 그리디
        - [] 정수론

# 8일차
1. 코딩테스트 학습
    - 자료구조
    -알고리즘
        - [] 장수론
        - [] 그래프 활용