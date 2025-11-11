def two_power(n: int):
    power = 0
    while 1:
        if n // 2**power > 1:
            power += 1
        else:
            return power


def main():
    while 1:
        m, n = [int(x) for x in input().split()]
        if m == 0 and n == 0:
            break
        power_m, power_n = two_power(m), two_power(n)
        remain_m, remain_n = m % (2**power_m), n % (2**power_n)
        part1 = 2**(power_n - power_m) - 1
        part2 = max(min(2**(power_n - power_m), remain_n - remain_m*2**(power_n - power_m) + 1),0)
        ans = part1 + part2
        print(ans)


if __name__ == '__main__':
    main()