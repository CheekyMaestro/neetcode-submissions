class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        already = []
        for i in nums :
            if i in already:
                return True
            already.append(i)
        return False
        
