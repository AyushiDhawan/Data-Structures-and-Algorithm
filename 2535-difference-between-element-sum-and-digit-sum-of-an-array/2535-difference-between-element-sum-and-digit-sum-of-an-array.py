class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        elements_sum= sum(nums)
        digits_sum= 0
        for num in nums:
            while num > 0:
                 digits_sum += num % 10 
                 num //= 10 
        return abs(elements_sum- digits_sum)
 

        