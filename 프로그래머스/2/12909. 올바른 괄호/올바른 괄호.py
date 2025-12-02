def solution(s):
    answer = True
    
    """
        ( 나왔다면 )가 있어야한다.
        1. stack 을 사용해서 ( 넣기
        2.1 ) 나오면 pop()
        2.2 pop()할 stack이 없으면 false
        3. stack에 빈 배열이 아니면 false
    """
    
    stacks = []
    for stack in s:
        if stack == '(':
            stacks.append(stack)
        else:
            if len(stacks) == 0:
                answer = False
                break
            elif stacks.pop() == '(' and stack != ')':
                answer = False
                break
                
    if len(stacks) != 0:
        answer = False
        

    return answer