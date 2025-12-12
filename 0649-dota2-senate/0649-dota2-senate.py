from collections import deque
class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        
        # R 정당, D 정당 나누어 index 저장
        r_senate = deque()
        d_senate = deque()
        n = len(senate)

        for i in range(len(senate)):
            if senate[i] == 'R':
                r_senate.append(i)
            else:
                d_senate.append(i)
        
        # R 이랑 D 어떤 index 더 큰지 비교하여 발업권 부여하거 발탁
        while r_senate and d_senate:
            r_senate_index = r_senate.popleft()
            d_senate_index = d_senate.popleft()

            # 0,1 0 
            if r_senate_index > d_senate_index:
                d_senate.append(d_senate_index + n)
            else:
                r_senate.append(r_senate_index + n)
        

        # 정당 승자 누구인지 리턴
        if r_senate:
            return 'Radiant'
        else:
            return 'Dire'
