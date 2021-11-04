# 완성하지 못했습니다.... 
 
def solution(msg):
    answer = []

    dic = {chr(i+65): i+1 for i in range(26)} # 사전 초기화 A~Z 모두 담기

    cnt = 0
    i = 0
    word = ''
    while i < len(msg):
        word += msg[i]
        print('1111',msg[i], word)
        word_end = 0
        while len(msg) - i > 0:
            if len(word) == 1 and dic[word] not in answer: # 한 글자인데, 아직 사용하지 않았으면
                answer.append(dic[word])
                if i+1 < len(msg):
                    word += msg[i+1]
                    dic[word] = 27 + cnt
                print('hi')
                break

            else:    # 한 글자인데 이미 사용했거나, 두 글자 이상이면

                while len(msg) - word_end > 0:
                    word_end += 1
                    print(dic[word], word)

            dic[word] = 27 + cnt

        i += 1
        word = ''

    return answer


solution('KAKAO')
# solution('TOBEORNOTTOBEORTOBEORNOT')


# git commit -m "code: Solve programmers 압축 (yeonju)"