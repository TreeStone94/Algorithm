import heapq

def solution(jobs):
    jobs.sort()  # 요청시간 기준으로 정렬
    heap = []  # (소요시간, 요청시간) 형태로 저장
    current_time = 0
    total_time = 0
    total_count = len(jobs)

   # 작업이_남아있거나_힙이_비어있지않을때
    while jobs or heap:
        # 현재 시간에 실행 가능한 작업들을 힙에 추가
        while jobs and jobs[0][0] <= current_time:
            request_time, duration = jobs.pop(0)  # 맨 앞 작업 꺼내기
            heapq.heappush(heap, (duration, request_time))  # 힙에 추가

        # 힙에서 소요시간이 가장 짧은 작업 선택
        if heap:
            duration, request_time = heapq.heappop(heap)
            current_time = current_time + duration
            total_time += (current_time - request_time)
        # 실행할 작업이 없으면 시간 점프
        else:
            current_time = jobs[0][0]

    return total_time // total_count