from typing import List

class Solution1:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        res = [x**2 for x in nums]
        res = sorted(res)
        return res

class Solution2:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left_index = 0 
        right_index = len(nums)-1
        sorted_nums_index = len(nums)-1
        sorted_nums = [None] * len(nums)

        while sorted_nums_index >= 0:
            left_squre = (nums[left_index])**2
            right_squre = (nums[right_index])**2
            if left_squre >= right_squre:
                sorted_nums[sorted_nums_index] = left_squre
                sorted_nums_index -= 1
                left_index += 1 
            else:
                sorted_nums[sorted_nums_index] = right_squre
                sorted_nums_index -= 1
                right_index -= 1

        return sorted_nums


if __name__ == '__main__':
    nums = [-4,-1,0,3,10]

    #解法1: 简答粗暴
    s1 = Solution1()
    res1 = s1.sortedSquares(nums)
    print(res1)
    
    #解法2: 双指针 两边互相
    s2 = Solution2()
    res2 = s2.sortedSquares(nums)
    print(res2)  
    