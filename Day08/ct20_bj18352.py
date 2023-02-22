# 백준 18352 - 특정거리도시 찾기

import sys
from collections import deque
input = sys.stdin.readline # 입력 속도를 빠르게

N, M, K, X = map(int, input().split()) #노드수,예지수,목표거리,시작번호

A = [[] for _ in range(N+1)]
answer = [] # 값 담을 리스트
visited = [-1] * (N+1) # 방문리스트 초기화

def BFS(v):
    q = deque()
    q.append(v)
    visited[v] += 1
    while q:
        now = q.popleft() # 값을 뺸다
        for i in A[now]:
            if visited[i] == -1: # 한번도 미방문이면
                visited[i] = visited[now] + 1 # 거리값이 증가
                q.append(i)

#두번쨰 줄부터 엣지 입력
for _ in range(M):
    s, e = map(int, input().split())
    A[s].append(e)

BFS(X) # 시작점부터 BFS시작

for i in range(N+1):
    if visited[i] == K:
        answer.append(i)

if not answer:
    print(-1)
else:
    answer.sort()
    for i in answer:
        print(i)