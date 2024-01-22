# 二分查找
# 示例 1：
nums = [-1,0,3,5,9,12]
target = 9


def search(nums, target):
    length = len(nums)
    # 设置一个区间范围：
    left = 0
    right = length - 1
    
    # 检查区间是否有效
    while left <= right:
        # 取中间数:
        mid = left + (right - left) // 2 #这样计算是为了防止溢出，如果 left 和 right 都是非常大的正整数，那么 left + right 可能会超过整数的最大值，从而导致整数溢出。这种情况在某些编程语言和环境中是可能发生的，特别是在整数有固定大小的环境中，如 C++ 或 Java。
        if nums[mid] == target:
            print(mid)
            return mid
            break
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
        
    return -1


if __name__ == '__main__':
    search(nums=nums, target=target)


