def solution(array, commands):
    answer = []
    for c in commands:
        i = c[0]
        j = c[1]
        k = c[2]
        split_arry = sorted(array[(i-1):j])
        answer.append(split_arry[k-1])
    return answer