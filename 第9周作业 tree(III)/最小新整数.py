def increasing_monotonic_stack(nums, k):
    stack = []
    count = 0
    for i in range(len(nums)):
        while stack and int(stack[-1]) > int(nums[i]):
            stack.pop()
            count += 1
        if count == k:
            stack.append(nums[i:])
            break
        stack.append(nums[i])

    for _ in range(k - count):
        stack.pop()
    return stack


def main():
    t = int(input())
    for _ in range(t):
        n, k = input().split()
        result = increasing_monotonic_stack(n, int(k))
        print(''.join(result))


if __name__ == '__main__':
    main()