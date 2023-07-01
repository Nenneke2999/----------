def solve(nums: list, target: int) -> list:
    
    storage = {}
    
    for i in range(len(nums)):

        add = target - nums[i]
        
        if add in storage:

            return [storage[add], i]
        
        storage[nums[i]] = i
    
    return None

nums = [3, 4, 2]

if __name__=='__main__':
    print(solve(nums, 5))
