def solution(numbers, target):
    def dfs(index, current_sum):
        if index == len(numbers):
            return 1 if current_sum == target else 0
        count = 0
        count += dfs(index+1, current_sum + numbers[index])
        
        count += dfs(index+1, current_sum - numbers[index])
        
        return count
    return dfs(0,0)