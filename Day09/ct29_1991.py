# 백준 1991 - 트리순회
import sys
input = sys.stdin.readline

N =int(input())
tree = {} # 딕셔너리

for _ in range(N):
    root, left, right = input().split()
    tree[root] = [left,right]

def preOrder(now): #후위 순회
    if now == '.':return
    print(now, end='')
    preOrder(tree[now][0]) # 왼쪽 노드 탐색
    preOrder[tree[now][1]] # 오른쪽 노드 탐색

def inOrder(now): #후위 순회
    if now == '.':return
    inOrder(tree[now][0]) # 왼쪽 노드 탐색
    print(now, end='')
    inOrder[tree[now][1]] # 오른쪽 노드 탐색

def postOrder(now): #후위 순회
    if now == '.':return
    postOrder(tree[now][0]) # 왼쪽 노드 탐색
    postOrder[tree[now][1]] # 오른쪽 노드 탐색
    print(now, end='')# 부모노드 출력

preOrder('A')
print()
inOrder('A')
print()
postOrder('A')