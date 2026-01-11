def solution(k, dungeons):
    answer = -1
    # k: 유저의 현재 피로도
    # 던전별 정보: [최소 필요 피로도, 소모 피로도]
    
    # 1. 첫번째 던전을 먼저 탐험하고 두번째나 세번째을 탐험했을 때
    # 2. 두번째 던전을 먼전 탐험하고 첫번째나 세번째를 탐험했을 때
    # 3. 세번째 던전을 먼저 탐험하고 첫번째나 두번째를 탐험했을 때
    
    # 던전 진입
    # n, 던전방문
    n = len(dungeons)
    in_dungeons = [False] * n
    
    def in_dungeon(current_k, count):
        nonlocal answer
        answer = max(answer, count)
        
        for i in range(n):
            if not in_dungeons[i] and dungeons[i][0] <= current_k:
                in_dungeons[i] = True
                in_dungeon(current_k - dungeons[i][1], count + 1)
                in_dungeons[i] = False
            
    
    in_dungeon(k, 0)
    # 최대값을 구하는게 필요
    return answer # 유저가 탐험 할 수 있는 최대 던전수