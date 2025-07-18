def solution(n):
    answer = []
    number = 2
    while n > 1:
        if n % number == 0:
            answer.append(number)
            n = n // number
        else:
            number += 1
            while True:
                # 소수인지 판별
                for i in range(2, int(number ** 0.5) + 1):
                    if number % i == 0:
                        number += 1
                        break
                else:
                    break  # 소수라면 while 탈출
    return sorted(list(set(answer)))
