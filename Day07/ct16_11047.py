# 백준 11047
# 데이터리스트 내부의 동전을 이용해서 최소한의 갯수로 정해진 금액을 맞추기

N, K = map(int,input().split()) # N은 동전 갯수, K는 목표 금액
A = [0] * N # 동전 데이터 리스트

for i in range(N): #i가 데이터 리스트 갯수만큼 돔
     A[i] = int(input())  # N개의 동전 금액을 입력

count = 0

for i in range(N-1, -1, -1): # n-1을 -1씩 -1까지 돌린다
    if A[i] <= K: # 만약 A[i]가 K보다 작으면
        count += int(K /A[i]) # 목표금액을 A[i]만큼 나누고 count에 더해라
        K = K % A[i] # K의 나머지 금액

print(count) # 동전 갯수