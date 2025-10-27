class solution:
    def feibonaqie(self, n):
        feibo_list = [0, 1, 1]
        if n >= 3:
            for i in range(2, n):
                feibo_list.append(feibo_list[i-2]+feibo_list[i-1]+feibo_list[i])
        return feibo_list[n]


if __name__ == '__main__':
    num = int(input())
    solut = solution()
    print(solut.feibonaqie(num))