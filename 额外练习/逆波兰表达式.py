from math import trunc


class Solution:
    def evalRPN(self, tokens) -> int:
        stack = []
        sign = ['+','-','*','/']
        for i in tokens:
            if i in sign:
                b,a = stack.pop(),stack.pop()
                cal_result = trunc(eval(''.join([a,i,b])))
                stack.append(str(cal_result))

            else:
                stack.append(i)
        return int(stack[0])


if __name__ == '__main__':
    solut = Solution()
    str_to_solut = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
    print(solut.evalRPN(str_to_solut))