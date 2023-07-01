def isBrokenVersion(x: int) -> bool:
    if x < 4:
        return False
    else: 
        return True

def solve(n: int) -> int:
    
    low = 1
    high = n
    mid = (low + high) // 2
    res = -1
    
    while low <= high:

        if isBrokenVersion(mid):
            
            res = mid
            high = mid - 1
            mid = (low + high) // 2

        else:
            
            low = mid + 1
            mid = (low + high) // 2
    
    if res == -1:
        return high
    else:
        return res


assert(solve(7) == 4)