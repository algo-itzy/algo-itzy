import sys
input = sys.stdin.readline

for _ in range(int(input())):
    zero = [1, 0]
    one = [0, 1]
    n = int(input())

    for i in range(2, n+1):
        zero.append(zero[i-1] + zero[i-2])
        one.append(one[i-1] + one[i-2])

    print(zero[n], one[n], sep=' ')

"""
결과 또한 피보나치 수열을 따르고 있어서, 피보나치 재귀 함수를 이용했더니 시간 초과가 났습니다.

"""