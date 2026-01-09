def solution(numbers):
    
    # 1,2,3
    # 조합할 수 있는 수의 열을 만들기 (재귀함수), 중복제거
    # 1,1,3
    # 1 -> 1하고 나머지 2,3 조합 1, 12, 13, 123
    # 2 -> 2하고 나머지 1,3 조합 1, 11
    
    # 중복제거 
    nums = set()
    def make_numbers(current, remain_numbers):
        if current:
            nums.add(int(current))
            
        for i in range(len(remain_numbers)):
            make_numbers(
                current + remain_numbers[i],
                remain_numbers[:i] + remain_numbers[i+1:]   
            )
    # O(n)
    make_numbers('', numbers)
    
    # 소수를 찾는 함수
    # 1이 아니여도 되고, 2로 나누었을때 나머지가 0이 아니고, 홀수로 나누었을때도 나머지가 0이 아닌 수를 소수
    # O(n)
    def is_prime(n):
        if n == 1: return False
        elif n == 2: return True
        elif n % 2 == 0: return False
        
        for i in range(3, int(n**0.5)+1, 2):
            if n % i == 0:
                return False
        return True
    # 조합한 수의열에서 소수만 찾아서 리턴
    return sum(1 for n in nums if is_prime(n))