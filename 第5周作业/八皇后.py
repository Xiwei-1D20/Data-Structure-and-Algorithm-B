def backtracking(index_x,index_y,chessboard_all,path):
    chessboard = [[0 for _ in range(8)] for _ in range(8)]
    path = path*10 + index_x + 1
    if index_y == 7:
        return path
    else:
        for i in range(index_y+1,8):
            chessboard[i][index_x] = 1
        xiexian1 = min(8-index_x, 8-index_y)
        for i in range(1,xiexian1):
            chessboard[index_y + i][index_x + i] = 1
        xiexian2 = min(index_x+1,8-index_y)
        for i in range(1,xiexian2):
            chessboard[index_y + i][index_x - i] = 1
        chessboard_all.append(chessboard)
        for i in range(8):
            safe = 0
            for j in chessboard_all:
                if j[index_y + 1][i] == 1:
                    safe += 1
            if safe == 0:
                temp = backtracking(i, index_y + 1, chessboard_all, path)
                if temp:
                    result.append(temp)
        chessboard_all.pop()
        return 0


#n = int(input())
chessboard = [[0 for _ in range(8)] for _ in range(8)]
result = []
for i in range(8):
    ans = backtracking(i,index_y=0,chessboard_all = [],path=0)
n = int(input())
for i in range(n):
    print(result[int(input())-1])