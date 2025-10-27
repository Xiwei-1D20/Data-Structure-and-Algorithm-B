from codecs import replace_errors
from math import expm1
from operator import truediv


def is_number(s):
    try:
        int(s)
        return True
    except ValueError:
        pass
    return False

class Solution:
    def decodeString(self, s: str) -> str:
        string_coding = list(s)
        i = len(string_coding)-1
        #倒着遍历。检查到数字时，向后检查的方括号一定属于这个数字，避免判断方括号的归属
        while i > -1:
            #检查某一位是否为数字
            if is_number(string_coding[i]) == 1:
                k = i
                #若是，继续向前找更多数字，确定重复次数
                while is_number(string_coding[k]) == 1:
                    k -= 1
                    if k == -1:
                        break
                repeat_number = int(''.join(string_coding[k+1:i+1]))
                j = i+1
                #向后找方括号
                while string_coding[j] != ']':
                    j += 1
                #解码
                str_decode = ''.join(string_coding[i+2:j]*repeat_number)
                i = k+1
                del string_coding[i:j+1]
                string_coding.insert(i,str_decode)
            i -= 1
        return ''.join(string_coding)


if __name__ == '__main__':
    solut = Solution()
    str_to_solut = input()
    print(solut.decodeString(str_to_solut))
