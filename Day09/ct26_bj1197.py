#백준 1197 - 최소신장트리 구하기
# 시간 복잡도 0(e*log(e))
import sys
from queue import PriorityQueue
input = sys.stdin.readline

N,M = map(int, input().split())
pq = PriorityQueue()
parent = [0] * (N+1)

#유니온파인드를 위한 대표노드 리스트 초기화
for i in range(N+1):
    parent[i] = i

for i in range(M): # 엣지 개수만큼 입력
    s,e,w = map(int, input().split())
    pq.put((w,s,e))

def find(a):
    if a == parent[a]:
        return a
    else:
        parent[a] = find(parent[a])
        return parent[a]

def union(a, b):
    a = find(a)
    b = find(b)
    if a != b:
        parent[b] = a

useEdge = 0
result = 0

while useEdge < N - 1:  #mst는 항상 N-1
    w, s, e = pq.get()
    if find(s) != find(e): # 같은 부모가 아닐 경우만 연결
        union(s, e)
        result += w
        useEdge += 1 #  중요 !! 유니온일 경우만 1 증가

print(result)