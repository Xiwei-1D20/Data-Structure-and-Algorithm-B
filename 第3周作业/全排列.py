class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        n = len(nums)
        permuted_array = []
        current = []
        def backtrack(index, current):
            if index == n:
                permuted_array.append(nums[:])
            else:
                for i in range(index, n):
                    current.append(nums[i])
                    backtrack(index + 1)
                    nums[index], nums[i] = nums[i], nums[index]
        backtrack(index=0)
        return permuted_array

if __name__ == '__main__':
    solution = Solution()
    print(solution.subsets([1, 2, 3, 4]))
