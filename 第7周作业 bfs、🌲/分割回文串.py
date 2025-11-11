from collections import deque
from typing import List, Optional

class Solution:
    def partition(self, s: str) -> list[list[str]]:
        def is_palin(s):
            if s == s[::-1]:
                return True
            else:
                return False
        palin = set()
        s_len = len(s)
        for sub_len in range(1, s_len + 1):
            for j in range(0, s_len - sub_len + 1):
                if is_palin(s[j:j+sub_len]):
                    palin.add(s[j:j+sub_len])
        result = []

        def backtrack(index_left, trace):
            for i in range(index_left+1, s_len + 1):
                if s[index_left:i] in palin:
                    trace.append(s[index_left:i])
                    if i == s_len:
                        result.append(trace[:])
                    else:
                        backtrack(i, trace)
                    trace.pop()
        backtrack(0, trace=[])
        return result

if __name__ == "__main__":
    solution = Solution()
    print(solution.partition('aab'))