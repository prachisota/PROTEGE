class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        final=[]
        for i in nums1:
            if i in final:
                pass
            elif i in nums2:
                final.append(i)
            else:
                pass
        return final
