from typing import List

#暴力解法:
class Solution1:
    def removeElement(self, nums: List[int], val: int) -> int:
        nums_length = len(nums)   
        i = 0
        while i < nums_length:
            if nums[i] == val:
                for j in range(i+1, nums_length):
                    nums[j-1] = nums[j]
                i-=1
                nums_length-=1 
            i+=1
        return nums_length


# 双指针快慢指针解法:
'''
快指针: 用于扫描目标数组的所有element.
慢指针: 用于指向所有新数组的更新后的位置.
'''
class Solution2:
    def removeElement(self, nums: List[int], val: int) -> int:
        nums_length = len(nums)   
        slow_index = 0 
        for fast_index in range(nums_length):
            if nums[fast_index] != val:
                nums[slow_index] = nums[fast_index]
                slow_index += 1
        return slow_index


if __name__ == '__main__':
    nums = [3,2,2,3]
    val = 2

    # 暴力解法:
    print("这个是暴力解法的结果")
    s = Solution1()
    nums_length = s.removeElement(nums, val)
    print(nums_length, nums[:nums_length])

    print()

    #快慢指针解法
    print("这个是快慢指针解法的结果")
    s2 = Solution2()
    nums_length = s2.removeElement(nums, val)
    print(nums_length, nums[:nums_length]) 