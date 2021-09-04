# 와 입출력... 짜증쓰
# 188ms

from sys import stdin, stdout

read = stdin.readline
write = stdout.write

# 리턴을 활용하고 싶어서 함수화했습니다.
def AC(arr, p):
    pop_cnt = p.count("D")

    # pop이 n보다 크면 에러 출력
    if pop_cnt > n:
        return "error"
    # pop과 n 사이즈가 같을 때 빈 배열 출력
    elif pop_cnt == n:
        return "[]"
    
    # R을 경계로 pop 횟수 출력
    pops = p.split("R")
    pop_lefts, pop_rights = 0, 0
    for i, pop in enumerate(pops):
        if i%2:
            pop_rights += len(pop)
        else:
            pop_lefts += len(pop)

    # popleft, popright 만큼 scope 좁혀서 slicing
    # -0 인덱싱 예외 처리
    if pop_rights == 0:
        result = arr[pop_lefts:]
    else:
        result = arr[pop_lefts:-pop_rights]

    # 홀수번 뒤집어서 pops 원소가 짝수개 이면, 결과를 뒤집어 줌
    if not len(pops)%2:
        result = list(reversed(result))
    
    return "["+",".join(result)+"]"


if __name__ == "__main__":
    T = int(read())

    for _ in range(T):
        p, n = read().rstrip(), int(read())
        rd = read()
        arr = []

        if n > 0:
            arr = rd[1:-2].split(",")

        write(AC(arr, p)+'\n')

# git commit -m "code: Solve boj 05430 AC (yoonbaek)"