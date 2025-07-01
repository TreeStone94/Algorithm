def solution(numbers):
    snumbers = sorted(numbers)
    answer = snumbers[-1] * snumbers[-2]
    return answer