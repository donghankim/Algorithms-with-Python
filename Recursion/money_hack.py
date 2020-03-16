"""
You are a bank account hacker.Initially you have 1 rupee in your account, and you want exactly N rupees in your account.You wrote two hacks, First hack can multiply the amount of money you own by 10, while the second can multiply it by 20. These hacks can be used any number of time . Can you achieve the desired amount N using these hacks.

retreived from:
https://www.hackerearth.com/practice/basic-programming/recursion/recursion-and-backtracking/practice-problems/algorithm/hack-the-money/
"""

def hack_possible(amount: int) -> bool:

    if amount == 1:
        return True

    elif amount == 0:
        return False

    elif amount%10 == 0:
        if hack_possible(amount//10) == True:
            return True
        else:
            return hack_possible(amount//20)

    elif amount%20 == 0:
        if hack_possible(amount//20) == True:
            return True
        else:
            return hack_possible(amount//10)

    else:
        return False


# test case
print(hack_possible(0))
print(hack_possible(1))
print(hack_possible(2))
print(hack_possible(200))



