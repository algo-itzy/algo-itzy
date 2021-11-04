# git commit -m "code: Solve programmers 압축 (seungkyu)"
def solution(msg):
    answer = []
    msg_lst = list(msg)
    dic = {f'{chr(i+64)}': i for i in range(1, 27)}
    num = 27
    i = 0
    
    while i < len(msg):
        if i == len(msg)-1:
            answer.append(dic[msg[-1]])
            i += 1
        else:
            j = i+1
            while msg[i:j] in dic:
                if j == len(msg)+1:
                    break
                j += 1
                
            answer.append(dic[msg[i:j-1]])
            
            if j < len(msg)+1:
                dic[''.join(msg[i:j])] = num
                
                num += 1
                i += j-i-1
            
    return answer