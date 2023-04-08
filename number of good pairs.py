class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count=0
        appeared=[]
        for i in nums:
            if i not in appeared :
                appeared.append(i)
                #add the value which appears once
            elif i in appeared:
                #means its a pair
                count+=1
        return count
