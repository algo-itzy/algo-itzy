T = int(input())

for tc in range(1, T + 1):
    N, hexa = map(str, input().split())
    N = int(N)
    digit = []
    for i in range(N):
        d = ord(hexa[i]) - ord('0') if '0' <= hexa[i] <= '9' else ord(hexa[i]) - ord('A') + 10
        # print(d)
        output = ""
        for j in range(3, -1, -1):
            output += '1' if d & (1 << j) else '0'
        for k in range(len(output)):
            digit.append(int(output[k]))

    print("#{}".format(tc), end=' ')
    for h in digit:
        print(h, end='')
    print()
