class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        all_possible_parenthesis = []

        def add_parenthesis(all: list):
            cur = set()
            for i in all[-1]:
                cur.add(i + '()')
                cur.add("()" + i)
                cur.add('(' + i + ')')
            if len(all) > 2:
                for i in range(1, len(all) - 1):
                    for j in all[i]:
                        for k in all[len(all) - i - 1]:
                            cur.add(j + k)
            return cur

        all_possible_parenthesis.append({'()'})
        if n > 1:
            for i in range(2, n + 1):
                cur = add_parenthesis(all_possible_parenthesis)
                all_possible_parenthesis.append(cur)
        ans = list(all_possible_parenthesis[-1])
        return ans

if __name__ == '__main__':
    solut = Solution()
    print(solut.generateParenthesis(15))