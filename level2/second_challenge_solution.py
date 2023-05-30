from itertools import permutations
def solution2(L):
    L.sort(reverse=True)
    for length in range(len(L), 0, -1):
        for perm in permutations(L, length):
            num = int(''.join(map(str, perm)))
            if num % 3 == 0:
                return num
    return 0
print(solution2([3,1,4,1]))
print(solution2([3, 1, 4, 1, 5, 9])) 