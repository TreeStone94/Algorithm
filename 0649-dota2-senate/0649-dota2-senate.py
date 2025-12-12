from collections import deque

class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        # 각 정당의 상원의원 인덱스를 저장하는 큐
        radiant = deque()
        dire = deque()
        n = len(senate)
        
        # 초기 인덱스 설정
        for i, s in enumerate(senate):
            if s == 'R':
                radiant.append(i)
            else:
                dire.append(i)
        
        # 한 쪽이 모두 제거될 때까지 반복
        while radiant and dire:
            r_index = radiant.popleft()
            d_index = dire.popleft()
            
            # 더 앞선 순서(작은 인덱스)가 상대를 제거
            if r_index < d_index:
                # Radiant가 이김 - 다음 라운드를 위해 큐 뒤에 추가
                radiant.append(r_index + n)
            else:
                # Dire가 이김 - 다음 라운드를 위해 큐 뒤에 추가
                dire.append(d_index + n)
        
        # 남아있는 쪽이 승리
        return "Radiant" if radiant else "Dire"