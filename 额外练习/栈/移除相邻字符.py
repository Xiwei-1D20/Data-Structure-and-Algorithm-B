class Solution:
    def resultingString(self, s: str) -> str:
        stack = ['0']
        for i in s:
            if self.is_continue(stack[-1], i):
                stack.pop()
            else:
                stack.append(i)
        return ''.join(stack[1:])

    def is_continue(self, a, b):
        if abs(ord(a) - ord(b)) == 1 or abs(ord(a) - ord(b)) == 25:
            return True
        return False


if __name__ == '__main__':
    solut = Solution()
    print(solut.resultingString("zadb"))