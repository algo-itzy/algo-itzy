'''
1. 글자수로 먼저 구분 => 글자수에 따라 리스트 구분(이중리스트)
2. 같은 글자 수 내에서 정렬 => sorted이용
3. 최대 50자임에 유의
4. set 이용?
5. sort만 이용?
'''

def solve() :
    n = int(input())
    # 범위 설정 조심 - 최대 50자이므로 words[50]가 존재하도록
    words = [[] for _ in range(51)]

    for _ in range(n) :

        word = input()
        len_word = len(word)

        if word not in words[len_word] :
            words[len_word].append(word)
    
    for i in range(1, 51) : # 범위 설정 조심 (최대가 50이 되도록)

        if words[i] != [] :
            print(*sorted(words[i]), sep='\n')

if __name__ == '__main__' :
    solve()
