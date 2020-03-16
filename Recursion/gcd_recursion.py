# find the greatest common divisor (GCD) using recursion -> Euclidean algorithm

def gcd(a, b: int) -> int:
    if a == b:
        return a

    else:
        if a > b:
            return gcd(a-b, b)
        else:
            return gcd(b-a, a)

# test case
print(gcd(45, 10))
print(gcd(1, 5))
print(gcd(1701, 3768))
