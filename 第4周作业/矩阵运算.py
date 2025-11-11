class MyMatrix:
    def __init__(self, data):
        self.data = data
        self.rows = len(data)
        self.cols = len(data[0])

    def __matmul__(self, other):
        if len(self.data[0]) != len(other.data):
            raise ValueError('Error!')

        result = [[0 for x in range(len(other.data[0]))] for x in range(len(self.data))]
        for i in range(self.rows):
            for j in range(self.cols):
                for k in range(other.cols):
                    result[i][k] += self.data[i][j] * other.data[j][k]
        return MyMatrix(result)

    def __add__(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError('Error!')
        result = []
        for i in range(self.rows):
            row = [self.data[i][j] + other.data[i][j] for j in range(self.cols)]
            result.append(row)
        return MyMatrix(result)


    def __str__(self):
        return f'{self.data}'

    def __getitem__(self, index):
        return self.data[index]


class Solution:
    def matrix_cal(self, matrix):
        try:
            result = MyMatrix(matrix[0]) @ MyMatrix(matrix[1])
            result = result + MyMatrix(matrix[2])
            return [result, row[0]]
        except ValueError:
            pass
            return 'Error!'


if __name__ == '__main__':
    solution = Solution()
    matrix = [[], [], []]
    row = []
    col = []
    for i in range(3):
        temp = [int(x) for x in input().split()]
        row.append(temp[0])
        col.append(temp[1])
        for j in range(temp[0]):
            matrix[i].append([int(x) for x in input().split()])
    ans = solution.matrix_cal(matrix)
    if ans == 'Error!':
        print(ans)
    else:
        for i in range(ans[1]):
            print(' '.join([str(x) for x in ans[0][i]]))


            #感想：在add中没有直接用列表推导式，而是每一个index都算了一遍并append进result，似乎这里导致内存溢出了