# 테스트 케이스의 갯수 N을 입력 받음
N = int(input())

for i in range (N) : 
    string = input()
    string += " "
    stack = []
    for j in string :
        # j 값이 공백이 아니면 stack 이 빌 때까지 내용을 출력시키게끔
        if j != " " :
            stack.append(j)
        else :
            while stack : 
                # end='' 로 설정하여, 줄 바꾸지 않도록
                print(stack.pop(), end ='')
            #단어와 단어 간 띄어쓰기 
            print(' ', end ='')
