dict = {}
def solution(k, room_number):
#   room_number 원하는 방 번호
#   k 방의 개수
    answer = [] # 배정된 방 번호
    
    for r in room_number:
        answer.append(find(r))
    
    return answer

def find(n):
    path = []
    while n in dict:
        path.append(n)
        n = dict[n]
    for p in path:
        dict[p] = n + 1
    dict[n] = n + 1
    return n
