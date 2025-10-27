class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        n = len(nums)
        subset_array = [[]]
        def backtrack(index, current):
            if index != n:
                for i in range(index, n):
                    current.append(nums[i])
                    subset_array.append(current[:])
                    backtrack(i + 1, current)
                    current.pop()
        backtrack(index=0, current=[])
        return subset_array

if __name__ == '__main__':
    solution = Solution()
    print(solution.subsets([]))