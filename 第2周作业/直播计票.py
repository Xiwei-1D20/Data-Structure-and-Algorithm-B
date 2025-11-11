class solution:
    def vote_counting(self, vote):
        vote_list = list(map(int, vote.split()))
        vote_count = dict()
        max_count = 0
        for i in range(len(vote_list)):
            if vote_list[i] not in vote_count.keys():
                vote_count[vote_list[i]] = 1
            else:
                vote_count[vote_list[i]] += 1
        for key in vote_count.keys():
            if vote_count[key] > max_count:
                max_count_index = [key]
                max_count = vote_count[key]
            elif vote_count[key] == max_count:
                max_count_index.append(key)
        return ' '.join([str(x) for x in sorted(max_count_index)])


if __name__ == '__main__':
    vote1 = input()
    Solution = solution()
    print(Solution.vote_counting(vote1))
