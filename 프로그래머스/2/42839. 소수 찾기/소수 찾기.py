def solution(numbers):
    nums = set()
    
    # 재귀로 순열 생성
    def make_permutation(current, remaining):
        if current:
            nums.add(int(current))
        
        for i in range(len(remaining)):
            make_permutation(
                current + remaining[i],
                remaining[:i] + remaining[i+1:]
            )
    
    make_permutation('', numbers)
    
    # 소수 판별
    def is_prime(n):
        if n < 2:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        for i in range(3, int(n**0.5) + 1, 2):
            if n % i == 0:
                return False
        return True
    
    return sum(1 for num in nums if is_prime(num))