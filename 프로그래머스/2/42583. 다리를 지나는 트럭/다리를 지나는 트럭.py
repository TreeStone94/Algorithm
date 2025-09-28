import collections

def solution(bridge_length, weight, truck_weights):
    answer = 0
    
    # 1. 필요한 변수들 초기화
    bridge = collections.deque([0] * bridge_length)
    truck_weights = collections.deque(truck_weights)
    current_bridge_weight = 0

    # bridge 큐가 존재할 동안 계속 반복 (시간이 흐름)
    while bridge:
        answer += 1 # 1초 경과

        # 2. 다리 끝에 도달한 트럭 내리기
        finished_truck = bridge.popleft()
        current_bridge_weight -= finished_truck

        # 3. 대기 트럭이 있다면, 다리에 올릴지 결정
        if truck_weights:
            if current_bridge_weight + truck_weights[0] <= weight:
                # Case 1: 트럭을 올릴 수 있음
                new_truck = truck_weights.popleft()
                bridge.append(new_truck)
                current_bridge_weight += new_truck
            else:
                # Case 2: 무게 초과로 못 올림
                bridge.append(0) # 빈 공간을 추가
    
    return answer