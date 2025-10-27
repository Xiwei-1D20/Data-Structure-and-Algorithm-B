import string


def backtrack(index_x, index_y, chessboard, count, row_x, row_y, path):
    # 标记骑士走过的位置：
    chessboard[index_x][index_y] = 1

    # count达标时，将坐标记录至path，结束递归。
    if count == row_x * row_y - 1:
        # 注意要复原棋盘
        chessboard[index_x][index_y] = 0
        path.append([index_y, index_x])
        return path

    # count未达标，则在八个方向上遍历并递归。如果某次递归返回的path不为[]，说明骑士已经完全走遍棋盘。
    # 此时，可以将当前位置append到棋盘内，结束本轮递归
    else:
        for i in range(8):
            temp_index_x = index_x + direct[i][0]
            temp_index_y = index_y + direct[i][1]
            if chessboard[temp_index_x][temp_index_y] == 0:
                backtrack(temp_index_x, temp_index_y, chessboard, count+1, row_x, row_y, path)
                if path:
                    path.append([index_y, index_x])
                    chessboard[index_x][index_y] = 0
                    return path
        chessboard[index_x][index_y] = 0


class Solution:
    def subsets(self, nums):
        all_result = []
        for i in range(nums):
            # 初始化chessboard。往上下、左右额外添加两行/列避免out of index
            chessboard_rows, chessboard_cols = [int(x) for x in input().split()]
            chessboard = [[1 for _ in range(chessboard_cols+4)] for _ in range(chessboard_rows+4)]
            for i in range(2, chessboard_rows+2):
                for j in range(2, chessboard_cols+2):
                    chessboard[i][j] = 0
            # 遍历矩阵作为骑士的初始位置，并开始递归
            for j in range(2, chessboard_cols + 2):
                for i in range(2, chessboard_rows+2):
                    result = backtrack(i, j, chessboard, count=0, row_x=chessboard_rows, row_y=chessboard_cols, path=[])
                    # 这一连串break丑丑的（
                    if result:
                        all_result.append(result)
                        break
                if result:
                    break
            if result:
                continue
            else:
                all_result.append([])
        return all_result


if __name__ == '__main__':
    solution = Solution()

    # 初始化骑士走的方向。注意骑士的走向需要按字典序排列以满足题目的要求。
    direct = [[-1, -2], [1, -2], [-2, -1], [2, -1], [-2, 1], [2, 1], [-1, 2], [1, 2]]

    # 输入参数、输出答案
    nums = int(input())
    ans = solution.subsets(nums)
    letter = list(string.ascii_uppercase)
    num_in_ans = 0
    for i in ans:
        i.reverse()
        path_str = ''
        if i:
            for j in i:
                path_str += ''.join([letter[j[0]-2], str(j[1]-1)])
        else:
            path_str += 'impossible'
        num_in_ans += 1
        print(f'Scenario #{num_in_ans}:')
        print(path_str)
        if num_in_ans != nums:
            print()
