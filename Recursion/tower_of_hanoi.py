# return the number of moves it takes to solve tower of hanoi given number of disks
# check this link for more details https://www.geeksforgeeks.org/c-program-for-tower-of-hanoi/

global moves
moves = 0

def tower_moves(n: int) -> int:
    global moves

    if n == 1:
        moves += 1
        return

    else:
        tower_moves(n - 1)
        tower_moves(n - 1)
        moves += 1

# this method explains how the disks are moving --> not working...
def tower_description(n: int, from_, aux, target: str):
    if n == 1:
        print(f"Moving disk: {n} from {aux} to {target}")
        return

    else:
        tower_description(n-1, from_, target, aux)
        print(f"Moving disk: {n} from {from_} to {aux}")
        tower_description(n-1, target, aux, from_)


# test case
tower_moves(3)
print(moves)

tower_description(3, "A", "B", "C")


