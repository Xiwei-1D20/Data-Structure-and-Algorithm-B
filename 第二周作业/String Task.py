class solution:
    def Task(self, string):
        vowels = ["a", "o", "y", "e", "u", "i"]
        for i in range(len(string)-1,-1,-1):
            if string[i] in vowels:
                string.pop(i)
        return '.'+'.'.join(string)



if __name__ == '__main__':
    String_for_deal = list(input().lower())
    Solution = solution()
    print(Solution.Task(String_for_deal))