def solution(numbers, direction):
    answer = [0] * len(numbers)
    
    for i in range(len(numbers)):
        if direction == 'right':
            answer[(i + 1) % len(numbers)] = numbers[i]
        else:
            answer[(i - 1) % len(numbers)] = numbers[i]
            
    return answer