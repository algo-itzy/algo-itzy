while True:

    N = input() 
    
    if N == '0': # 0 을 입력 받으면 종료
        break

    if N == N[::-1]: # 입력 받은 수가 그 수를 역순으로 했을 때와 같은지 비교
        print('yes')
    else:
        print('no')
    


# string = 'Hello, World!'
# reversed_str = string[::-1]
# print(reversed_str)



"""
git commit -m "code: Solve boj 01259 펠린드롬수 (yeonju)"
"""