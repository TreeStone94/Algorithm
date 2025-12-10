from collections import deque
def solution(bridge_length, weight, truck_weights):
    answer = 0
    # 다리를 건너는 트럭에 대한 선언
    brige_trunks = deque([0] * bridge_length)
    
    # 대기트럭 큐로 변경
    trucks = deque(truck_weights)
    
    # 다리이 올라간 트럭들의 합
    brige_truck_weight = 0
    
    # 대기트럭이다 없어질때 까지 시간 계산
    while brige_trunks:
        answer += 1  # 시간 1초 증가 (맨 위에)

      # TODO 1: 다리 맨 앞 트럭이 빠져나가는지 확인
      # brige_trunks.popleft() 했을 때 나온 값이 0이 아니면?
      # -> brige_truck_weight에서 빼줘야겠죠?
        brige_trunk = brige_trunks.popleft()
        if brige_trunk != 0:
            brige_truck_weight -= brige_trunk
        
      # TODO 2: 새 트럭을 다리에 올릴 수 있는지 확인
      # trucks가 있고 + (brige_truck_weight + 새트럭무게 <= weight) 이면?
      # -> trucks.popleft()해서 다리에 올리고
      # -> brige_trunks.append(트럭무게)
      # -> brige_truck_weight에 더하기
        if trucks and brige_truck_weight + trucks[0] <= weight:
            truck = trucks.popleft()
            brige_trunks.append(truck)
            brige_truck_weight += truck
      # TODO 3: 새 트럭을 못 올리면?
      # -> brige_trunks.append(0)  # 빈 공간
        elif trucks and brige_truck_weight + trucks[0] > weight:
            brige_trunks.append(0)

        
    return answer