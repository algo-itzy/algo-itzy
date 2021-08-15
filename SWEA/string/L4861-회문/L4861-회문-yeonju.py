""""
회문은 1개 - 가로 or 세로
"""

T = int(input()) # 테스트 케이스의 수 T

for tc in range(T):
    N, M = map(int, input().split()) # 가로와 세로의 길이  N  # 찾아야 하는 회문의 길이 M

    arr = [list(input()) for _ in range(N)] # string 을 한 글자 씩 끊어서 리스트에 담기 

    # 가로로 된 글자 찾을 때
    for i in range(0, N): # 행
        for j in range(0, N-M+1): # 열
            str =''

            for k in range(M//2):
                if arr[i][j+k] == arr[i][j+ (M-1) -k]:
                    str.append(arr[i])
                    
            else:
                print('같음')
                    


    # 세로로 된 글자 찾을 때
    for j in range(N):
        for i in range(0, N-M+1):
            for k in range(M//2):
                if arr[j+k][i] == arr[j+(M-1)-k][i]:


    
list = [[1,2,3,2,6],[3,4,5,6,7]]

str = ' '
strr= str + 'list[0][1]'
print(strr)