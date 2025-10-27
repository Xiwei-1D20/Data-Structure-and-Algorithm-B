class Solution:
    def model_sort(self, nums, model_list):
        model_list.sort(key = lambda name: name[0])
        model_dict = dict()
        # 创建字典套字典，第一个键为模型名称，第二个键为单位，预留模型大小的列表
        for j in range(nums):
            if model_list[j][0] not in model_dict.keys():
                model_dict[model_list[j][0]] = {'M': [], 'B': []}
            size = 0
            # 将模型大小归并到对应的模型和单位的字典内，储存为列表
            if float(model_list[j][1]) % 1 == 0:
                size = int(model_list[j][1])
            else:
                size = float(model_list[j][1])
            model_dict[model_list[j][0]][model_list[j][-1]].append(size)
        # 按照要求输出文本
        for key1 in model_dict.keys():
            str_result = ''
            for key2 in model_dict[key1].keys():
                model_dict[key1][key2].sort()
                for k in range(len(model_dict[key1][key2])):
                    str_result += f'{model_dict[key1][key2][k]}{key2}, '

            print(f'{key1}: ' + str_result[:-2])

if __name__ == "__main__":
    solution = Solution()
    nums1 = int(input())
    model_list1 = []
    for i in range(nums1):  # 将输入的模型进行处理，分成名称 大小 单位 三部分
        model = input().split('-')
        model.append(model[-1][-1])
        model[-2] = model[-2][:-1]
        model_list1.append(model)
    solution.model_sort(nums1, model_list1)
    #print(result)
