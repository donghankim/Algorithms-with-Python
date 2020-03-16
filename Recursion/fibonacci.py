# return the nth number in the Fibonacci sequence
# assume the sequence starts with index 1, not 0

def fibo(n: int) -> int:
    if n == 1 or n == 2:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)

# test case
print(fibo(1))
print(fibo(8))
print(fibo(10))


