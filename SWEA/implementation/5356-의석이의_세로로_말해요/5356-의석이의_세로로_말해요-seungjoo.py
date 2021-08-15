
def read_vertical(s):
    answer = ''
    cnt = 0
    while cnt <= 15:
        for string in s:
            if string:
                answer += string.pop(0)
        cnt+=1
    return answer


for test in range(1, int(input())+1):
    strings = list(list(input()) for _ in range(5))
    print(f'#{test} {read_vertical(strings)}')
