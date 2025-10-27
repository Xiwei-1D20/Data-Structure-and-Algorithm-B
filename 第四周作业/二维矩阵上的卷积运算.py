class Solution:
    def convolution(self, matrices, dimensions):
        rows_core, cols_core = dimensions[1][0], dimensions[1][1]
        rows_result, cols_result = dimensions[0][0]-dimensions[1][0]+1, dimensions[0][1]-dimensions[1][1]+1
        result = [[0 for x in range(cols_result)] for x in range(rows_result)]
        for i in range(rows_result):
            for j in range(cols_result):
                for k in range(rows_core):
                    for l in range(cols_core):
                        result[i][j] += matrices[0][i+k][j+l]*matrices[1][k][l]
        return result

if __name__ == '__main__':
    solution = Solution()
    matrices = []
    dimensions = []
    temp = [int(x) for x in input().split()]
    #存储矩阵和卷积核的大小
    dimensions.append([temp[0], temp[1]])
    dimensions.append([temp[2], temp[3]])
    #输入矩阵
    for rows, cols in dimensions:
        matrix = []
        for i in range(rows):
            matrix.append([int(x) for x in input().split()])
        matrices.append(matrix)
    #卷积
    ans = solution.convolution(matrices, dimensions)
    for i in range(dimensions[0][0]-dimensions[1][0]+1):
        print(' '.join([str(x) for x in ans[i]]))
