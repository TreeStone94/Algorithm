def solution(brown, yellow):
    total = brown + yellow
    
    for height in range(3, total):
        if total % height == 0:
            width = total // height
            
            # 가로 >= 세로 조건
            if width >= height:
                # yellow 개수 검증
                if (width - 2) * (height - 2) == yellow:
                    return [width, height]