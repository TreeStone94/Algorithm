def solution(clothes):
    answer = 1
    
    hash_map = {}
    for c in clothes:
        hash_map[c[1]] = hash_map.get(c[1], 0) + 1
    
    for name, count in hash_map.items():
        answer *= (count + 1)
    
    return answer - 1