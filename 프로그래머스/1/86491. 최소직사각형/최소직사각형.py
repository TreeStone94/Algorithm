def solution(sizes):
    for size in sizes:
        if size[1] > size[0]:
            size[0], size[1] = size[1], size[0]
    
    max_w = max(size[0] for size in sizes)
    max_h = max(size[1] for size in sizes)
    
    return max_w * max_h