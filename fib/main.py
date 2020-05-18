import time

start_time = time.time()

def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n - 1) + fib(n - 2)

# results = []
# for i in range(30):
#     results.append(fib(i + 1))

# print(results)
# print(f'fib: {(time.time() - start_time) * 1000}ms')
