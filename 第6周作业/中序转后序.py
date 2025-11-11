# 这个模块用于将符号和数字分割开
def seperate(s):
    result = []
    temp = ''
    for j in s:
        if j in ['+', '-', '*', '/', '(', ')']:
            if temp != '':
                result.append(temp)
                temp = ''
            result.append(j)
        else:
            temp += j
    if temp != '':
        result.append(temp)
    return result

# 局部的中序表达式转后续表达式
def middle_to_end(s):
    j = 0
    while j < len(s):
        if s[j] == '*' or s[j] == '/':
            s[j], s[j+1] = s[j+1], s[j]
            temp = ' '.join(s[j-1:j+2])
            del s[j-1:j+2]
            s.insert(j-1, temp)
            j -= 1
        j += 1
    j = 0
    while j < len(s):
        if s[j] == '+' or s[j] == '-':
            s[j], s[j+1] = s[j+1], s[j]
            temp = ' '.join(s[j-1:j+2])
            del s[j-1:j+2]
            s.insert(j-1, temp)
            j -= 1
        j += 1
    return s

# 使用栈的思想解决问题
def main():
    n = int(input())
    for i in range(n):
        origin = input()
        middle_num_and_sign = seperate(origin)
        stack = []
        j = 0
        while 1:
            if middle_num_and_sign[j] == '(':
                stack.append(j)
            elif middle_num_and_sign[j] == ')':
                index = stack.pop()
                temp = middle_to_end(middle_num_and_sign[index+1:j])
                del middle_num_and_sign[index:j+1]
                middle_num_and_sign.insert(index, temp[0])
                j -= (j - index + 1)
            j += 1
            if j == len(middle_num_and_sign):
                break
        print(' '.join(middle_to_end(middle_num_and_sign)))



if __name__ == '__main__':
    main()