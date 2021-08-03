'''
최대공약수 쉽게 구하는 법
a, b가 있을 때 % 로 나눠서 나머지로 바꾸고
계속해서 같은 작업진행
최소공배수는 나온 나머지들 곱*마지막 몫
'''

def input_func() :
    num1, num2 = map(int, input().split())
    return num1, num2

def get_gcd(num1, num2) : # 최대 공약수
    if num1 % num2 == 0 :
        return num2
    num1 = num1 % num2
    # num1, num2를 그냥 쓰면 num1 = num2 가 되버릴 수 있다...
    max_num = max(num1, num2)
    min_num = min(num1, num2)
    # 재귀함수에서 return으로 호출하지 않으면 값이 none으로 리턴됨
    # 리턴값이 필요한 경우 반드시 return 쓰기
    return get_gcd(max_num, min_num) 
 
def get_lcm(num1, num2, gcd_num) : # 최소 공배수, (최대 공약수 이용)
    return (num1 // gcd_num) * (num2 // gcd_num) * gcd_num

if __name__ == '__main__' :
    num1, num2 = input_func()
    gcd_num = get_gcd(max(num1, num2), min(num1, num2))
    lcm_num = get_lcm(num1, num2, gcd_num)
    print(gcd_num)
    print(lcm_num)