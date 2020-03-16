# reverse a given string using recursion

def reverse_string(string: str) -> str:

    if len(string) == 0:
        return ""

    else:
        return string[-1] + reverse_string(string[:-1])

# test cases
print(reverse_string("abc"))
print(reverse_string("nun"))
print(reverse_string("hello"))
















