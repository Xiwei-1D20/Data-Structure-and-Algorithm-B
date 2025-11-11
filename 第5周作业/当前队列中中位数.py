import bisect
def tryint(s):
    if s == int(s):
        return int(s)
    else:
        return s


n = int(input())
temp = []
sorted_list = []
length = 0
for i in range(n):
    handle = input().split()
    if handle[0] == "add":
        temp.append(int(handle[1]))
        bisect.insort(sorted_list, temp[-1])
        length += 1
    elif handle[0] == "query":
        if length % 2 == 0:
            print(tryint((sorted_list[length//2-1]+sorted_list[length//2])/2))
        else:
            print(sorted_list[length//2])
    elif handle[0] == "del":
        num_deled = temp.pop(0)
        index = sorted_list.index(num_deled)
        sorted_list.pop(index)
        length -= 1