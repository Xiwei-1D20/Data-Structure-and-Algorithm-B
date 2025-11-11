class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        left = ['[', '{', '(']
        Valid = ['[]', '{}', '()']
        res = ''
        for i in s:
            if i in left:
                stack.append(i)
            else:
                if stack == []:
                    return False
                res = stack.pop() + i
                if res in Valid:
                    continue
                else:
                    return False
        if stack == []:
            return True
        else:
            return False





if __name__ == '__main__':
    solut = Solution()
    text = '('
    result1 = solut.isValid(text)
    print(result1)