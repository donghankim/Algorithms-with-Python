# Algorithms with Python
Various algorithms implemented in python

## Introduction
The purpose of this repository is to help understand and implement various different algorithms. This repository will have the same structure as my data structure with python repository. I will provide a brief description of all the algorithms, and their analysis. Each algorithm will have their own folder in this repository, and examples of "coding interview" equestions regarding those algorithms will also be included in the folder. When doing complexity analysis, I will only explain the worst-case time complexity as that is the metric we are often interested in. I am creating this repository as I am writing all of the code and explanation, so make sure you check frequently!

If you find any errors or mistakes, feel free to email me or to request a push commit.

## Recursion
The basis of recursion is to solve large problems by breaking it into smaller problems of the original problem. Therefore, recursion often involves a function calling itself. However, before you start using recursion, there are three rules you need to follow.

### Three Laws of Recursion
1. A recursive algorithm must have a base case(will be exaplained with an example).
2. The recursive algorithm must always change state, and move towards the defined base case.
3. A recursive algorithm must call itself.

To really understand the three laws of recursion, lets consider an example problem that can be solved using recursion.

### Sum of Digits
Given a number, return the sum of all of its individual digits. For example, if the input digit is 1234, then our solution should return 1 + 2 + 3 + 4 which is 10.

```python
def sum_of_digits(number: int) -> int:

    # base case
    if number == 0:
        return 0

    else:
        #recursive element
        return number % 10 + sum_of_digits(number // 10)


# test case
print(sum_of_digits(12))  # prints 3
print(sum_of_digits(123))  # prints 6
print(sum_of_digits(1000))  # prints 1
```

From this example, the base case simply helps the recursive algorithm to terminate. Otherwise, the function will run forever. The line after the else statement satisfies the second law because, when we recursively call the sum_of_digits function again, it does so after dividing the current number by 10. Therefore, its helping the function go closer to the base case.

Recursion can be a little difficult to understand. Looking at the execution sequence of the function above can help you understand how recursion works a little better. This is the execution sequence of the code above:
```
sum_of_digits(1234)
-> 4 + sum_of_digits(123)                                  # 4 + 6 -> 10 returned
          -> 3 + sum_of_digits(12)                         # 3 + 3
                    -> 2 + sum_of_digits(1)                # 2 + 1
                              -> 1 + sum_of_digits(0)      # 1 + 0
```
So technically the actual addition of the sum happens when the function reaches the base case. After the base case is reached, the function works its way up adding the appropriate values, and therefore returning 10. The best way to understand recursion is to solve some recursion problems on your own. Check out the Recursion folder to see some practice questions that I solved using recursion.

## Search Algorithms (list-based)
Searching is a very common task in computer science. Some search algorithms answer the question of membership (whether a certain value is in a list), while other search algorithms tell us where the element being searched is located (the index). There are multiple search algorithms out there, and in this repository, I will try to cover the most frequently used ones.

### Sequential Search
Sequential search is performed on a list-based data structure, where elements in the list are stored relative to one another. This is the most basic search algorithm. In the example below, we will assume that the list is arranged in random order (in other words, not sorted). This is an important factor that I will explain in a bit.

```python
from typing import List

# sequential search -> unsorted list
def seq_search(target: int, nums: List[int]) -> bool:

    for i in range(len(nums)):
        if nums[i] == target:
            return True

    return False

```

You can modify the code above to return not only a boolean, but also the index at which the target value is in the list. However, for the analysis of sequential search, it doesnt make a difference. As the code above shows, sequential search compares each element in the given list with the target value. Therefore, regardless of whether the target is in the list or not, this algorithm runs at O(n).

If the list given is <strong>sorted</strong> in ascending order, then the <strong>best-case</strong> time complexity for when the item is <em>not</em> in the list is improved from O(n) to O(1). This is becasue if the target value is 3 and the first item on the list is 4, then we already know that 3 cannot be in the list as the list is sorted. However, for an unsorted list, we would still have to check all of the elements in the list. Do note that this is only for the best-case scenario, for when the item is not in the list.

### Binary Search
Binary search is an improvement of sequential search. Binary search is also used for list-based data structure, where elements in the list are stored relative to one another. Binary search only works on lists that has already been sorted.

```python
from typing import List

def binary_search(target: int, nums: List[int]) -> int:

    start_index = 0
    end_index = len(nums) -1

    while start_index <= end_index:
        mid_index = (start_index + end_index) // 2
        if nums[mid_index] == target:
            return True

        elif target < nums[mid_index]:
            end_index = mid_index - 1

        else:
            start_index = mid_index + 1

    return False

```

Will be updated soon.




