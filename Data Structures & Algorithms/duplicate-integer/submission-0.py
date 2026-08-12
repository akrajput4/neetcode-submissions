class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dict1={}
        for item in nums:
            if dict1.get(item):
                return True
            else:
                dict1[item]=1

        return False            
        
        