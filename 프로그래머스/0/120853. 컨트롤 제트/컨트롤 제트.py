def solution(s):
    # split으로 문자열을 배열로 만듬
    # stack으로 사용하면 됨
    
    s = list(s.split())
    intS = []
    for inS in s:
        if inS == 'Z':
            intS.pop()
        else:
            intS.append(int(inS))

    answer = sum(intS)
    return answer