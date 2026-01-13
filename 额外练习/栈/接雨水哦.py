class Solution:
    def trap(self, height: list[int]) -> int:
        stack = []
        ans = 0
        for i in range(len(height)):
            index1 = i
            if not stack or height[index1] < stack[-1][0]:
                stack.append((height[index1], i))
            else:
                temp = 0
                min_delta_height = height[i]
                while stack:
                    if height[i] >= stack[-1][0]:
                        col, index0 = stack.pop()
                        delta_height = height[i] - col
                        # 使用index1 避免重复相加
                        temp += delta_height * (index1 - index0)
                        index1 = index0
                        min_delta_height = min(min_delta_height, delta_height)
                    else:
                        break
                else:
                    # 减去左边漏掉的
                    temp -= min_delta_height * (i - index0)
                stack.append((height[i], index0))
                ans += temp
        return ans


if __name__ == '__main__':
    solut = Solution()
    print(solut.trap([4,2,0,3,2,5]))