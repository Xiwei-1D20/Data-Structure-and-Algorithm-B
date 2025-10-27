def merge_sort(arr, os_times):
    if len(arr) <= 1:
        return arr, os_times

    # 分解：将列表分成两半
    mid = len(arr) // 2
    left_half, os_times = merge_sort(arr[:mid], os_times)  # 递归排序左半部分
    right_half, os_times = merge_sort(arr[mid:], os_times)  # 递归排序右半部分

    # 合并：将两个有序子列表合并
    return merge(left_half, right_half, os_times)

def merge(left, right, os_times):
    sorted_arr = []
    i = j = 0

    # 比较两个子列表的元素，按顺序合并
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_arr.append(left[i])
            i += 1
        else:
            sorted_arr.append(right[j])
            j += 1
            os_times += (len(left) - i)

    # 将剩余的元素添加到结果中
    sorted_arr.extend(left[i:])
    sorted_arr.extend(right[j:])
    return [sorted_arr, os_times]

# 示例
while 1:
    n = int(input())
    if n == 0:
        break
    arr = []
    for i in range(n):
        arr.append(int(input()))
    #arr = [1,2,3]
    #arr = [9, 1, 0, 5, 4]
    sorted_arr = merge_sort(arr, os_times=0)
    print(sorted_arr[1])