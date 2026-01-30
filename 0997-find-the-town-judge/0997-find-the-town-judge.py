class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        
        """
        어느 마을에 1부터 n까지 번호가 매겨진 n명의 사람이 살고 있습니다. 이 중 한 명이 비밀리에 마을 판사라는 소문이 돌고 있습니다.

        마을 판사가 존재한다면, 다음 두 가지 조건이 성립합니다:

        1. 마을 판사는 누구도 신뢰하지 않습니다.
        2. 마을 판사를 제외한 모든 사람이 마을 판사를 신뢰합니다.
        조건 1과 2를 모두 만족하는 사람은 정확히 한 명이다.
        신뢰 관계 배열 trust가 주어지며, trust[i] = [ai, bi]는 ai라는 번호를 가진 사람이 bi라는 번호를 가진 사람을 신뢰함을 나타낸다. 신뢰 배열에 신뢰 관계가 존재하지 않는다면, 그러한 신뢰 관계는 실제로 존재하지 않는다.

        마을 판사가 존재하고 식별할 수 있다면 마을 판사의 번호를 반환하고, 그렇지 않으면 -1을 반환하라.
        """


        # 2차원 배열에서 ai번호에 판사가 있으면 안된다
        # 모든 사람이 판사 bi 신뢰한다.

        # 4 [[1,2],[1,3]]

        # 사용자 신뢰를 했는지 여부 배열
        user_trust = [1 for i in range(n)]
        
        # 신뢰를 했으면 여부 배열 체크
        for t in trust:
            ai = t[0]
            user_trust[ai-1] = 0
        
        # 여부 체크한것중에 남아있는 사람이 있으면 그사람이 판사, 없으면 -1
        print(user_trust)
        if user_trust.count(1) > 0:
            p = user_trust.index(1) +1
            count = 0
            for t in trust:
                bi = t[1]
                if p == bi:
                    count +=1
            if count == n-1:
                return p
            else:
                return -1
        else:
            return -1

