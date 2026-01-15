def solution(phone_book):    
    hash_map = {}
    for p in phone_book:
        hash_map[p] = 1
    
    for p in phone_book:
        temp = ""
        for c in p:
            temp += c
            
            if temp in hash_map and temp != p:
                return False
    return True