class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        stack = [(10000, -1)]
        ans = [0] * len(temperatures)
        index = 0
        while index < len(temperatures):
            while temperatures[index] > stack[-1][0]:
                _, index_before = stack.pop()
                ans[index_before] = index - index_before
            else:
                stack.append((temperatures[index], index))
                index += 1
        return ans

if __name__ == '__main__':
    solut = Solution()
    solut.dailyTemperatures([30,40,50,60])