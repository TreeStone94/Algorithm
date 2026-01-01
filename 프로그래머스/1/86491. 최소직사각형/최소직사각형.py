def solution(sizes):
    # 큰값은 가로길이로, 작은 값은 세로 길이로 sizes 변경
    for i in range(len(sizes)):
        if sizes[i][0] < sizes[i][1]:
            sizes[i][0], sizes[i][1] = sizes[i][1], sizes[i][0]
    
    # 가로의 최대값, 세로의 최대값
    max_w = max(size[0] for size in sizes)
    max_h = max(size[1] for size in sizes)
    
    return max_w * max_h