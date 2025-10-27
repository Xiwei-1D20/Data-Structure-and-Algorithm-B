def main():
    n, nums_m1, nums_m2 = [int(x) for x in input().split()]
    m1 = []
    m2 = []
    dict_m1 = {}
    dict_m2 = {}
    # 输入并储存行号/列号的index
    for i in range(nums_m1):
        temp = [int(x) for x in input().split()]
        if temp[0] in dict_m1.keys():
            dict_m1[temp[0]].append(i)
        else:
            dict_m1[temp[0]] = [i]
        m1.append(temp)
    for i in range(nums_m2):
        temp = [int(x) for x in input().split()]
        if temp[1] in dict_m2.keys():
            dict_m2[temp[1]].append(i)
        else:
            dict_m2[temp[1]] = [i]
        m2.append(temp)
    ans = []
    # 检测i、j是否在对应字典中存在，如果存在，再进行遍历
    for i in range(n):
        for j in range(n):
            temp = 0
            if i in dict_m1.keys() and j in dict_m2.keys():
                for k in range(n):
                    i_k = None
                    j_k = None
                    for i1 in dict_m1[i]:
                        if m1[i1][1] == k:
                            i_k = i1
                            break
                    for j1 in dict_m2[j]:
                        if m2[j1][0] == k:
                            j_k = j1
                            break
                    if i_k is not None and j_k is not None:
                        temp += m1[i_k][2] * m2[j_k][2]
            if temp:
                ans.append([i, j, temp])
    for i in ans:
        print(' '.join([str(x) for x in i]))


if __name__ == '__main__':
    main()
