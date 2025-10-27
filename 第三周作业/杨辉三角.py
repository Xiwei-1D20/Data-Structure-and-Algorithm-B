class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        ans = []
        first_two = [[1],[1, 1]]
        for i in range(min(numRows, 2)):
            ans.append(first_two[i])
        for i in range(2, max(2, numRows)):
            Row = [1]
            for j in range(1, i):
                Row.append(ans[i-1][j-1]+ans[i-1][j])
            Row.append(1)
            ans.append(Row)
        return ans


if __name__ == '__main__':
    solution = Solution()
    print(solution.generate(5))
