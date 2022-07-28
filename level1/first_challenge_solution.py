#solution(x, y): compares the lists and returns the additional ID.
def solution(x,y):
    additional_id = set(x).symmetric_difference(set(y))
    return next(iter(additional_id))



# TEST
print(solution([13, 5, 6, 2, 5], [5, 2, 5, 13]))