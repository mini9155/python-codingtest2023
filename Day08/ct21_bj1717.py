# 숫자가 작은 쪽이 대표 노드가 된다
# 만약 노드가 연결되어 있을 시 find는 연결된 대표 노드로 간다
import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)
N, M = map(int, input().split())
parent = [0] * (N+1)

def find(a): # find 연산
    if a == parent[a]: # 만약 a가 parent[a]랑 같으면
        return a 
    else: 
        parent[a] = find(parent[a]) # 재귀호출 -> 경로 압축
        return parent[a]

def union(a,b): # 대표 노드끼리 합치기
    a = find(a)
    b = find(b)
    if a != b:
        parent[b] = a
def checksame(a,b): # 둘이 같은 집합인지
    a = find(a)
    b = find(b)
    if a == b:  
        return True 
    return False

for i in range(0,N+1):
    parent[i] = i # 1,1 2,2 3,3 4,4 5,5 6,6 7,7

for i in range(M):
    question,a ,b = map(int, input().split()) # 0 1 3 or 1 1 7
    if question == 0:
        union(a,b)
    else:
        if checksame(a,b):
            print("Yes")
        else:
            print("No")