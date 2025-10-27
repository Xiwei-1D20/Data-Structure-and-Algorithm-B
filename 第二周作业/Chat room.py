class solution:
    def hello_right_or_not(self, wrong_hello):
        right_hello = ['h','e','l','l','o']
        index_start = 0
        index_end = len(wrong_hello)
        right_index = 0
        for i in range(5):
            for j in range(index_start, index_end):
                if right_hello[i] == wrong_hello[j]:
                    index_start = j + 1
                    right_index += 1
                    break
        if right_index == 5:
            return 'YES'
        else:
            return 'NO'


if __name__ == '__main__':
    hello = list(input())
    solut = solution()
    print(solut.hello_right_or_not(hello))