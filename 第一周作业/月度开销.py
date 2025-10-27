
class Solution:
    def minicost(self, day, month, cost_list) :
        left = max(cost_list)  #使用二分查找获得合适的最大的cost
        right = sum(cost_list)
        while left <= right:
            mid = (right + left)//2
            month_needed = 1
            cost_per_month = 0
            for j in range(day):
                if cost_per_month + cost_list[j] <= mid:
                    cost_per_month += cost_list[j]
                else:
                    cost_per_month = cost_list[j]
                    month_needed += 1
            if month_needed <= month:
                right = mid - 1
            elif month_needed > month:
                left = mid + 1
        return left



if __name__ == "__main__":
    solution = Solution()

    day1, month1 = list(map(int, input().split()))
    cost_list1 = []
    for i in range(day1):
        cost_list1.append(int(input()))
    result = solution.minicost(day1, month1, cost_list1)
    print(result)

