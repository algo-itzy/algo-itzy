zero = [1,0,1]           # fibo(0)일 때, fibo(1), fibo(2)일 때 0과 1의 개수
one = [0,1,1]

def fibo(n):
    length = len(zero)
    if n >= length:
        for i in range(length, n+1):
            zero.append(zero[i-1] + zero[i-2])
            one.append(one[i-1]+ one[i-2])
    print(f'{zero[n]} {one[n]}')


T = int(input())        # 테스트 케이스 개수 T

for _ in range(T):      # 테스트 케이스의 개수만큼 피보나치 함수를 실행 
    fibo(int(input())) 


"""
fibo(n)의 0과 1 호출 횟수는 
fibo(n-1)의 0과 1 호출 횟수 + fibo(n-2)의 0과 1의 호출 횟수의 합이랑 같음
            """
            
        
        
