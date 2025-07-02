import sys
sys.setrecursionlimit(10**7)

dict = {}
def solution(k, room_number):
#   room_number 원하는 방 번호
#   k 방의 개수
    answer = [] # 배정된 방 번호
    
    for r in room_number:
        answer.append(find(r))
    
    return answer

def find(n):
    if n in dict:
        dict[n] = find(dict[n])
        return dict[n]         
    else:
        dict[n] = n+1
        return n
