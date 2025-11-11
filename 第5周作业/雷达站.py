from math import sqrt

case = 0
while 1:
    try:
        data = input().split()
        if not data:
            continue
        n, d = map(float, data)
        n = int(n)
        if n == 0 and d == 0:
            break
        case += 1
        list_Radar_Installation = []
        switch = 0
        for i in range(n):
            x, y = map(float, input().split())
            if y > d or y < 0:
                switch = 1
            else:
                x_min = x - sqrt(d**2-y**2)
                x_max = x + sqrt(d**2-y**2)
                list_Radar_Installation.append([x_min, x_max])
        list_Radar_Installation.sort(key = lambda x: x[1])
        ans = 1
        if switch == 1:
            print(f'Case {case}: -1')
            continue
        x_max_now = list_Radar_Installation[0][1]
        for i in range(n):
            if list_Radar_Installation[i][0] > x_max_now:
                ans += 1
                x_max_now = list_Radar_Installation[i][1]
        print(f'Case {case}: {ans}')
    except EOFError:
        break



