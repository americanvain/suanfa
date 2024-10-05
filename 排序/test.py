from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        nums_zong =[0]+[nums[0]]+[]*(n-2)
        res =n
        exist =0

        for i in range(1,n):
            nums_zong.append(nums_zong[-1]+nums[i])
        
        # print(nums_zong)

        right,left=1,0

        # while right<n+1:
        #     while nums_zong[right]-nums_zong[left]<target:
        #         right+=1
        #     while nums_zong[right]-nums_zong[left]>=target:
        #         exist =1
        #         res = min(right-left,res)
        #         left+=1

        # if exist==0:
        #     return 0
        # else :
        #     return res
        while right<=n:
            if nums_zong[right]-nums_zong[left]<target:
                right+=1
            else:
                while nums_zong[right]-nums_zong[left]>=target:
                    exist =1
                    res = min(right-left,res)
                    left+=1         
        if exist==0:
            return 0
        else :
            return res

ret = Solution().minSubArrayLen(7,[8])

out = str(ret)
print(out)