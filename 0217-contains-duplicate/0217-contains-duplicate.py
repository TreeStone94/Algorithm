class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # 어떻게 하면 중복된 값이 있는지 체크를 할수 있을까?
        if len(set(nums)) == len(nums):
            return False
        else:
            return True