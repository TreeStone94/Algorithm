def solution(phone_book):
    answer = True
    # 현재 번호가 다른 번호의 앞에 붙어서 동일한지
    hash_map = {}
    for p in phone_book:
        hash_map[p] = 1
    
    
    for p in phone_book:
        temp = ''
        for number in p:
            temp += number
            
            if temp in hash_map and temp != p:
                return False
            
    return answer