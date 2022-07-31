# 1 <= h <= 30
# 1 <= node <= 2^h-1
def solution(h, q):
    output=[]
    for node in q:
        start = 1
        end = 2**h -1 
        if (end == node): output.append(-1) 
        else:
            while(node >= 1):
                end = end - 1
                mid = start + (end - start)//2
                if(mid == node or end == node): 
                    output.append(end + 1)
                    break 
                elif (node < mid): end = mid
                else: start = mid
    return output



print(solution(3, [7, 3, 5, 1])) # -1,7,6,3
print(solution(5, [19, 14, 28])) #21,15,29