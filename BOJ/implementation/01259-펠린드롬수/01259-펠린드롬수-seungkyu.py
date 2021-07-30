import sys

def solve() :
    input = sys.stdin.readline

    while 1 :
        word = str(input().rstrip()) # readline으로 읽으면 개행까지 읽어옴 주의

        if word == '0' :
            break
        # 단어 뒤집는 행동 간단하게 word[::-1]로 구현 가능
        print('yes') if word == word[::-1] else print('no')

        # if word == word[::-1] :
        #     print('yes')
        # else :
        #     print('no')

if __name__ == '__main__' :
    solve()
