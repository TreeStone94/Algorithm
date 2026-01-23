class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
    
    # 정수 배열 nums가 주어집니다. 이 배열은 n개의 요소로 구성되어 있으며, 정수 k도 함께 주어집니다.
    # 길이가 k인 연속된 부분 배열 중 평균값이 최대인 배열을 찾아 그 값을 반환하세요.

    # [1,12,-5,-6,50,3] n=6, k=4

    # 평균값 배열
        average_nums = []
        n = len(nums)
        # n-k+1 순회하여 평균값
        # for i in range(n-k+1):
        #     average = 0
        #     for num in nums[i:k+i]:
        #         average += num
        #     average_nums.append(average/k)
            

        # 4개 연속합
        init_sum = sum(nums[:k])
        average_nums.append(init_sum/k)
        # 0번째 제외되고, 4번째 추가
        # 1번째 제외되고, 5번째 추가
        for i in range(n-k):
            init_sum = init_sum - nums[i] + nums[k+i]
            average_nums.append(init_sum/k)

        # print(average_nums)
        # (12,-5,-6,50)/4
        # (-5,-6,50,3)/4

        # 평균값 중의 최대값 리턴
        return max(average_nums)

