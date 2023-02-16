def fibonacci(n):
    if n ==0: return 0
    elif n==1: return 1
    else:
        return fibonacci(n - 1) + fibonacci(n-2) 
# n = 3
# fibonacci(n - 1) = 2 
print('피보나치 수 -> 0 1', end=' ')
for i in range(2,10):
    print(fibonacci(i), end=' ')