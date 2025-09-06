def solution(s):
    stack = list()
    for ch in list(s):
        if ch == '(':
            stack.append(ch)
        elif len(stack) == 0:
            return False
        else:    
            left = stack.pop()
            if ch != ')' and left == '(':
                return False
    
    if len(stack) == 0:
        return True
    else:
        return False