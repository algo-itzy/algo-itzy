import sys
input = sys.stdin.readline

c = 1000000007


def multiply(mtx1, mtx2):
    result = []

    for i in range(len(mtx1)):
        result.append([])
        for j in range(len(mtx2[0])):
            tmp = 0
            for k in range(len(mtx1[0])):
                tmp += mtx1[i][k] * mtx2[k][j]
            result[i].append(tmp % c)

    return result


def power(mtx, p):
    if p == 1:
        return mtx

    tmp = power(mtx, p//2)

    if p % 2:
        return multiply(multiply(tmp, tmp), mtx)
    else:
        return multiply(tmp, tmp)


n = int(input())
m = [[1, 1], [1, 0]]
print(power(m, n)[0][1])
