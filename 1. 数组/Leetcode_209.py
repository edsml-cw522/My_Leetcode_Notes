from typing import List

class Solution1:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        res = []
        for start_index in range(len(nums)):
            for end_index in range(start_index, len(nums)):
                res_sum = sum(nums[start_index:end_index+1])
                if res_sum >= target:
                    res.append(end_index+1-start_index)
                    break
                else:
                    continue
        if res:
            return min(res)
        else:
            return 0




if __name__ == '__main__':
    target = 7
    nums = [2,3,1,2,4,3]

    #暴力算法
    # s1 = Solution1()
    # res1 = s1.minSubArrayLen(target, nums)
    # print(res1)


    #滑动窗口算法：
    start_index = 0 
    res = int('inf') #设置一个最大的数
    for end_index in range(len(nums)):
        sum_res += nums[end_index]
        while sum_res >= target:
            subL = end_index - start_index + 1
            res = min(res, subL)
            

