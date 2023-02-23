#플로이드 워셜
# a = 1 , b =1  == 다 0이다 , 나머지는 무한대
# 인접 행렬로 표현

# for (1 ~ N): 경유지 K에 관해
#   for (1 ~ N): 출발노드 S에 관해
#       for (1 ~ N): 도착노드 E에 관해
#           D[S][E] = math.min(D[S][E],D[S][K] + D[K][E]) math.min 최소값을 리턴해줌 max는 최대값   

import sys
input = sys.stdin.readline

N = int(input()) # 도시개수 5
M = int(input()) # 노선개수 14
distance = [[sys.maxsize for j in range(N + 1)] for i in range(N + 1)]

for i in range(1, N+1):
    distance[i][i] = 0 # 인접행렬 초기화 , 같은 값들은 0으로 초기화

for i in range(M):
    s, e, v= map(int, input().split())
    if distance[s][e] > v: # 중복된 노선 중 더 저렴한 버스가 있으면
        distance[s][e] = v

#플로이드 워셜 시작!!
for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1 , N+1):
             # 경유지를 경유해서 오는 노선 비용이 더 저렴하면
            if distance[i][j] > distance[i][k] + distance[k][j]:
                distance[i][j] = distance[i][k] + distance[k][j]

for i in range(1, N+1):
    for j in range(1, N+1):
        if distance[i][j] == sys.maxsize:
            print(0, end=' ')
        else:
            print(distance[i][j], end=' ')
    print()