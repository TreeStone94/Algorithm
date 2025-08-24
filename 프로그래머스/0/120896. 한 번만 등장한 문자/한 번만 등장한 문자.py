def solution(s):
    hash_s = {}
    for c in s:
        if c in hash_s:
            hash_s[c] += 1
        else:
            hash_s[c] = 1
            
    answer = ''
    for h in hash_s:
        if hash_s[h] == 1:
            answer += h
    
    return "".join(sorted(answer))