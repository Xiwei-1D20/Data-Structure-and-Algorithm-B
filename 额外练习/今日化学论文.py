

class Solution:
    def decodeString(self, s: str) -> str:
        string_coding = list(s[1:])
        stack = []
        multi = 1
        res = ''
        for i in string_coding:
            if i == '[':
                if multi == 0:
                    multi += 1
                stack.append([multi,res])
                multi = 0
                res = ''
            elif i == ']':
                last_multi, last_res = stack.pop()
                res = last_multi*(last_res+res*multi)
                multi = 1
            elif self.is_number(i) == 1:
                multi = multi*10 + int(i)
            else:

                res = res + i
    def is_number(self,num):
        try:
            int(num)
            return True
        except ValueError:
            pass
        return False


if __name__ == '__main__':
    solut = Solution()
    str_to_solut = input()
    print(solut.decodeString(str_to_solut))
