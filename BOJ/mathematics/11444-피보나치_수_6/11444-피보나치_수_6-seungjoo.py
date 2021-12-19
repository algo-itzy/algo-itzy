# git commit -m "code: Solve boj 11444 피보나치 수 6 (seungjoo)"

def matrix_mult(a, b):
    ret = [[0 ,0], [0, 0]]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                ret[i][j] += (a[i][k] * b[k][j]) % MOD
    return ret


n = bin(int(input()))[2:]

MOD = 1000000007
base = [[1, 1], [1, 0]]
answer = [[1, 0], [0, 1]]

for i in range(1, len(n) + 1):
    if n[-i] == '1':
        answer = matrix_mult(answer, base)
    base = matrix_mult(base, base)
        
print(answer[0][1] % MOD)