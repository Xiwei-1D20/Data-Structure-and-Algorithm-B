def minicost(num, wood_need, cost_list):
    left = 0  # 使用二分查找获得合适的最大的cost
    right = max(cost_list)
    while left <= right:
        mid = (right + left) // 2
        wood_needed_in_mid = 0
        if mid == 0:
            return 0
        for j in range(num):
            wood_needed_in_mid += (cost_list[j]//mid)
        #print(mid, wood_needed_in_mid)
        if wood_needed_in_mid < wood_need:
            right = mid - 1
        elif wood_needed_in_mid >= wood_need:
            left = mid + 1
    return left - 1


def main():
    n, k = (int(x) for x in input().split())
    cost_list = []
    for i in range(n):
        cost_list.append(int(input()))
    cost = minicost(n, k, cost_list)
    print(cost)


if __name__ == '__main__':
    main()