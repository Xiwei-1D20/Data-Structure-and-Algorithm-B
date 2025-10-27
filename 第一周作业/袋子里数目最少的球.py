from math import ceil


class Solution:
    def minimumSize(self, nums: list[int], maxOperations: int) -> int:
        max_num_of_bag = len(nums) + maxOperations
        left = 0  #使用二分查找获得合适的每个小袋的最高球数
        right = max(nums)
        while left <= right:
            mid = left + ceil((right - left)/2)
            print(mid)
            sum_num_of_bag = 0
            num_of_bag = []
            for i in range(len(nums)):
                num_of_bag.append(ceil(nums[i]/mid))
                sum_num_of_bag += ceil(nums[i]/mid)
            if sum_num_of_bag > max_num_of_bag:
                left = mid + 1
            elif sum_num_of_bag < max_num_of_bag:
                right = mid - 1
                if right == 0:
                    return max([ceil(a / b) for a, b in zip(nums, num_of_bag)])
            else:
                return max([ceil(a / b) for a, b in zip(nums, num_of_bag)])
        return left


if __name__ == "__main__":
    solution = Solution()

    # 测试用例1: 基本示例
    print("测试用例1:")
    nums1 = [2, 4, 8, 2]
    max_operations1 = 4
    result1 = solution.minimumSize(nums1, max_operations1)
    print(f"nums={nums1}, maxOperations={max_operations1}")
    print(f"结果: {result1}")
    print()

    # 测试用例2: 单个元素
    print("测试用例2:")
    nums2 = [9]
    max_operations2 = 2
    result2 = solution.minimumSize(nums2, max_operations2)
    print(f"nums={nums2}, maxOperations={max_operations2}")
    print(f"结果: {result2}")
    print()

    # 测试用例3: 两个元素
    print("测试用例3:")
    nums3 = [7, 17]
    max_operations3 = 2
    result3 = solution.minimumSize(nums3, max_operations3)
    print(f"nums={nums3}, maxOperations={max_operations3}")
    print(f"结果: {result3}")
    print()

    # 测试用例4: 边界情况 - 零操作
    print("测试用例4:")
    nums4 = [100]
    max_operations4 = 0
    result4 = solution.minimumSize(nums4, max_operations4)
    print(f"nums={nums4}, maxOperations={max_operations4}")
    print(f"结果: {result4}")
    print()

    # 测试用例5: 所有元素相同
    print("测试用例5:")
    nums5 = [5, 5, 5, 5]
    max_operations5 = 3
    result5 = solution.minimumSize(nums5, max_operations5)
    print(f"nums={nums5}, maxOperations={max_operations5}")
    print(f"结果: {result5}")
    print()

    # 测试用例6: 需要精确分割
    print("测试用例6:")
    nums6 = [8]
    max_operations6 = 3
    result6 = solution.minimumSize(nums6, max_operations6)
    print(f"nums={nums6}, maxOperations={max_operations6}")
    print(f"结果: {result6}")
    print()

    # 测试用例7: 多个不同元素
    print("测试用例7:")
    nums7 = [4, 8, 12]
    max_operations7 = 3
    result7 = solution.minimumSize(nums7, max_operations7)
    print(f"nums={nums7}, maxOperations={max_operations7}")
    print(f"结果: {result7}")
    print()

    # 测试用例8: 极大数值
    print("测试用例8:")
    nums8 = [1000000000,1000000000,1000000000]
    max_operations8 = 1000000000
    result8 = solution.minimumSize(nums8, max_operations8)
    print(f"nums={nums8}, maxOperations={max_operations8}")
    print(f"结果: {result8}")
    print()

    # 测试用例8: 极大数值
    print("测试用例8:")
    nums8 = [1000000000, 1000000000, 1000000000]
    max_operations8 = 1000000000
    result8 = solution.minimumSize(nums8, max_operations8)
    print(f"nums={nums8}, maxOperations={max_operations8}")
    print(f"结果: {result8}")
    print()