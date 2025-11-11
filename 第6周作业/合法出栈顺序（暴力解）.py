
def main():
    n = int(input())
    result = 0

    def backtrack(push, pop, diff):
        nonlocal result
        if push == 0 and pop == 0:
            result += 1
        if diff > 0 and push > 0:
            backtrack(push, pop - 1, diff - 1)
            backtrack(push - 1, pop, diff + 1)
        elif diff > 0:
            backtrack(push, pop - 1, diff - 1)
        elif push > 0:
            backtrack(push - 1, pop, diff + 1)
    backtrack(push=n, pop=n, diff=0)
    print(result)


if __name__ == '__main__':
    main()