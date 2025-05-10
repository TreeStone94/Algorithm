def solution(num_list, n):
#   num_list를 n으로 나눈 2차원 배열을 만든다
#   num_list를 전체 순회해야 하므로 for문으로 작성
#   index가 n으로 나머지 값이 0이라면 다음배열에 append한다
#   배열 index에 대한 변수가 필요

    answer = [[0] * n for _ in range(len(num_list) // n)]
    for i in range(len(num_list)):
        answer[i//n][i % n] = num_list[i]
        
    return answer