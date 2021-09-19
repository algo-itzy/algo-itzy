for tc in range(1, int(input())+1):
    n, arr = input().split()

    print(f"#{tc}", end=' ')

    for x in arr:
        print(bin(int(f'0x{x}', 16))[2:].zfill(4), end='')

    print()

# 2진수로 바꾸고 '0b' 자르고 앞에 0 채우는 일련의 과정
# 출력부 더 다듬을 수 있지만 패쓰