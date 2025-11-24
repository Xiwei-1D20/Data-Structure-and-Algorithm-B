def build_tree(nums: list):
    trie = dict()
    for i in range(len(nums)):
        if i == 0:
            if len(nums) == 1:
                temp0 = 'NO'
            else:
                temp0 = dict()
            trie[nums[i]] = temp0
        elif i == len(nums)-1:
            temp0[nums[i]] = 'NO'
        else:
            temp1 = dict()
            temp0[nums[i]] = temp1
            temp0 = temp1
    return trie


def is_ok(tries: list, nums: list):
    for i in tries:
        temp_dict = i
        for j in range(len(nums)):
            if nums[j] in temp_dict.keys():
                temp_dict = temp_dict[nums[j]]
                if temp_dict == 'NO':
                    return 0
            elif j == len(nums) - 1:
                temp_dict[nums[j]] = 'NO'
            else:
                temp_dict1 = dict()
                temp_dict[nums[j]] = temp_dict1
                temp_dict = temp_dict1
    return tries


def main():
    n = int(input())
    for _ in range(n):
        t = int(input())
        temp = []
        for i in range(t):
            temp.append([int(x) for x in list(input())])
        temp.sort(key=len)
        tries = [build_tree(temp[0])]
        for i in range(1, len(temp)):
            temp1 = is_ok(tries, temp[i])
            if temp1 == 0:
                print('NO')
                break
            else:
                tries = temp1
        else:
            print('YES')


if __name__ == '__main__':
    main()
