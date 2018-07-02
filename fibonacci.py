# Print fibonacci sequence using memoization and recursive techniques

cache = {0: 1, 1: 1}


def fib(n):
    if n in cache:
        return cache[n]
    ret = fib(n-2) + fib(n-1)
    cache[n] = ret
    return ret


for i in range(20):
    print(fib(i))
