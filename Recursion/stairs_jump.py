"""
Simran is running up a staircase with N steps, and can hop(jump) either 1 step or 2 steps at a time.You have to count, how many possible ways Simran can run up to the stairs.

retreived from:
https://www.hackerearth.com/practice/basic-programming/recursion/recursion-and-backtracking/practice-problems/algorithm/simran-and-stairs/
"""

def num_ways(n: int) -> int:

    if n == 1:
        return 1

    elif n == 2:
        return 2

    else:
        return num_ways(n-1) + num_ways(n-2)

# test case
print(num_ways(2))
print(num_ways(5))
print(num_ways(10))


