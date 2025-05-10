def solution(numbers, k):
#   공은 한명씩 건너띄고 다음사람에게 던진다: index+2
#   마지막번호의 다음은 다시 index 0이다
#   공을 던진 횟수만큼 반복한다
#   numbers의 길이를 가진 변수가 있어야 한다
#   0 -> 2 -> 4 -> 6 -> 8 -> 10
#   0 -> 2 -> 1 -> 0 -> 2 -> 4
#   index가 길이보다 커지면 길이만큼 다시 뺀다

    index = 0
    l = len(numbers)
    for _ in range(k-1):
        index +=2
        if index > l:
            index -= l
            
    answer = numbers[index]
    return answer