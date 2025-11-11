class Solution:
    def invert(self):
        n = int(input())
        text = []
        invert_index = dict()
        for i in range(n):
            temp = input().split()
            text.append(temp)
        m = int(input())
        word_list = []
        for j in range(m):
            word_list.append(input())
            invert_index[word_list[-1]] = [0]
        for i in range(n):
            for j in range(1,int(text[i][0])+1):
                if text[i][j] in invert_index.keys():
                    if invert_index[text[i][j]][-1] != i+1:
                        invert_index[text[i][j]].append(i+1)
        return [invert_index, word_list]

if __name__ == '__main__':
    solution = Solution()
    result = solution.invert()
    for i in result[1]:
        if result[0][i] == [0]:
            print('NOT FOUND')
        else:
            print(' '.join([str(x) for x in result[0][i][1:]]))