ALP = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'  # chr() 모른다는 가정하의 풀이

def solution(msg):
    answer = []
    dic = {}

    for i in range(26):
        # dic[chr(65+i)] = i+1
        dic[ALP[i]] = i+1

    w, c = 0, 0
    
    while True:
        c += 1

        if c == len(msg):
            answer.append(dic[msg[w:c]])
            break
        if msg[w:c+1] not in dic:
            answer.append(dic[msg[w:c]])
            dic[msg[w:c+1]] = len(dic)+1
            w = c

    return answer