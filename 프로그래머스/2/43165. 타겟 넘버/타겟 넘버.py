def solution(numbers, target):
    def dfs(index, current_sum):
        # 모든 숫자를 다 사용했을 때
        if index == len(numbers):  # len(numbers)-1이 아니라 len(numbers)!
            if current_sum == target:
                return 1
            else:
                return 0
        
        # 현재 숫자를 더하는 경우
        count1 = dfs(index+1, current_sum + numbers[index])
        # 현재 숫자를 빼는 경우
        count2 = dfs(index+1, current_sum - numbers[index])
        
        return count1 + count2
    
    return dfs(0, 0)