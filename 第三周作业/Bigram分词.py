class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> list[str]:
        word_list = text.split()
        length = len(word_list)
        ans = []
        for i in range(length-2):
            if word_list[i] == first:
                if word_list[i+1] == second:
                    ans.append(word_list[i+2])
        return ans


if __name__ == '__main__':
    solut = Solution()
    text = "we will we will rock you"
    first = "we"
    second = "will"
    result1 = solut.findOcurrences(text, first, second)
    print(result1)