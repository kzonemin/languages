import sys

def fibonacci(n, memo={}):
    if n in memo:
        return memo[n]
    if n == 0:
        return 0
    if n == 1:
        return 1
    memo[n] = fibonacci(n-1, memo) + fibonacci(n-2, memo)
    return memo[n]

u = int(sys.argv[1])
r = 0
for i in range(u):
    r += fibonacci(i)
print(r)
