def solution(n):
    answer = []
    number = 2
    while n >= number:
        if n % number == 0:
            answer.append(number)
            n = n // number
        else:
            number += 1
            count = 0
            for i in range(2, number + 1):
                if number % i == 0:
                    count += 1
            if count > 1:
                number += 1
    return sorted(list(set(answer)))