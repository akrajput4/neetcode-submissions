class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        nums1=[0]*2*len(nums)
        # print(nums1)
        for i in range(len(nums)):
            nums1[i] = nums[i]
            nums1[i+len(nums)] = nums[i]
        return nums1

        
        