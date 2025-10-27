class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        i = 0
        j = 0
        while i < len(nums):
            if nums[i] == 0:
                while j < len(nums):
                    if nums[j] == 0:
                        j += 1
                    elif j < i:
                        j += 1
                    else:
                        nums[i], nums[j] = nums[j], nums[i]
                        break
            i += 1
            print(nums)



if __name__ == '__main__':
    solut = Solution()
    solut.moveZeroes([0,1,0,3,12])