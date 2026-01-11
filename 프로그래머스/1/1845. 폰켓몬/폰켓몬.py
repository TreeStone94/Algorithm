def solution(nums):
    hash_map = {}
    
    for num in nums:
        if num not in hash_map:
            hash_map[num] = hash_map.get(num,0)
    
    choice_n = len(nums)//2
    
    if len(hash_map) > choice_n:
        return choice_n
    else:
        return len(hash_map)