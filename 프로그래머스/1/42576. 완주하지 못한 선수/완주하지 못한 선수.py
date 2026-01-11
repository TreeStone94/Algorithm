def solution(participant, completion):
    
    hash_map = {}
    for p in participant:
        hash_map[p] = hash_map.get(p,0) +1
    
    for c in completion:
        hash_map[c] -= 1
    
    for name, count in hash_map.items():
        if count == 1:
            return name
