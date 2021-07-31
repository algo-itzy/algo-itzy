'''
수학적인 지식이 있으면 쉽게 풀 수 있는 문제
(프로그래머스 1단계에 비슷한 문제 있었음)
소수 개수 => 그 수의 제곱근까지만 검사하면 됨
1은 소수가 아님
'''
def solve() :
    prime_num_cnt = 0 # 소수 개수
    n = int(input())
    numbers = map(int, input().split())

    for number in numbers :
        prime_num_cnt += check_prime_number(number)

    print(prime_num_cnt)

def check_prime_number(number) : # 소수 검사하는 함수

    if number == 1 : # 1은 소수가 아님
        return 0

    # 1로는 무조건 나누어지므로 2부터 제곱근까지 나눠보기
    for num in range(2, int(number**(1/2))+1) : 
        if number % num == 0 :
            return 0
    return 1 # for문을 돌면서 나머지 없이 나눠지는 수 없으므로 소수

if __name__ == '__main__' :
    solve()
