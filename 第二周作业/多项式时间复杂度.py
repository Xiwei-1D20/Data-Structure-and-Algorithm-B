class solution:
    def Task(self, string):
        split1 = string.split('+')
        ans = 0
        for i in range(len(split1)):
            split2 = [int(x) for x in split1[i].split('n^') if x != '']
            if split2[0] > 0:
                ans = max(ans, split2[-1])
        return f'n^{ans}'



if __name__ == '__main__':
    String_for_deal = input()
    Solution = solution()
    print(Solution.Task(String_for_deal))