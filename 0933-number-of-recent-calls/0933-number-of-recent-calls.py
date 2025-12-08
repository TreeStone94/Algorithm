from collections import deque

class RecentCounter:
    """
    RecentCounter 클래스는 특정 시간 범위 내의 최근 요청 횟수를 계산합니다.

    RecentCounter 클래스를 구현하세요:
    RecentCounter() 최근 요청 횟수를 0으로 초기화합니다.
    int ping(int t) 시간 t(밀리초 단위)에 새로운 요청을 추가하고, 최근 3000밀리초(새로운 요청 포함) 동안 발생한 요청 횟수를 반환합니다. 구체적으로, [t -    3000, t] 구간(포함) 내에서 발생한 요청 수를 반환합니다.
    모든 ping 호출은 이전 호출보다 반드시 더 큰 t 값을 사용합니다.
    """

    def __init__(self):
        self.requests = deque()

    def ping(self, t: int) -> int:
        # 요청수 저장
        self.requests.append(t)

        # t -3000 보다 첫번째 큐가 작으면 pop
        while self.requests and self.requests[0] < t -3000:
            self.requests.popleft()

        # 카운트 리턴
        return len(self.requests)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)