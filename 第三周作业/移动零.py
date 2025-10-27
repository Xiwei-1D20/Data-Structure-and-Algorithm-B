class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        for i in range(len(nums)-1,-1,-1):
            if nums[i] == 0:
                nums.pop(i)
                nums.append(0)
        print(nums)


if __name__ == '__main__':
    solut = Solution()
    solut.moveZeroes([0])