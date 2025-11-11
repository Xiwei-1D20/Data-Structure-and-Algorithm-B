def edge(A:list,k):
    x=len(A[0]);y=len(A)
    for i in range(y):
        A[i]=[k]+A[i]+[k]
    A.append([k]*(x+2));A.insert(0,[k]*(x+2))
    return A

def backtrack(board, track, index_x, index_y, word, index_word):
    direc = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    if board[index_x][index_y] == word[index_word]:
        if index_word == len(word)-1:
            return True
        else:
            track[index_x][index_y] = 1
            for i in range(4):
                dx = direc[i][0]; dy = direc[i][1]
                if track[index_x+dx][index_y+dy] == 0:
                    if backtrack(board, track, index_x+dx, index_y+dy, word, index_word+1):
                        return True
            track[index_x][index_y] = 0
    return False

class Solution:
    def exist(self, board, word: str) -> bool:
        track = [[1 for _ in range(len(board[0])+ 2)] for _ in range(len(board) + 2)]
        for i in range(1, len(board) + 1):
            for j in range(1, len(board[0]) + 1):
                track[i][j] = 0
        board = edge(board, 1)
        for i in range(1, len(board)-1):
            for j in range(1, len(board[0])-1):
                if board[i][j] == word[0]:
                    if backtrack(board, track, i, j, word, index_word=0):
                        return True
        return False


if __name__ == "__main__":
    solution = Solution()
    print(solution.exist(board = [['A','B','C','E'],['S','F','C','S'],['A','D','E','E']], word = "ABCB"))