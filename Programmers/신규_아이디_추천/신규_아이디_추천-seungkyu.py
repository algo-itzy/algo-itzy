# git commit -m "code: Solve programmers 신규 아이디 추천 (seungkyu)"
def solution(new_id):
    new_id = new_id.lower()
    len_id = len(new_id)
    temp = ""
    
    for i in range(len_id):
        x = new_id[i]
        if ('a' <= x <= 'z' or '0' <= x <= '9' or x in '-_.'):
            temp += x
    new_id = temp
    
    while ".." in new_id:
        new_id = new_id.replace('..','.')
    
    if new_id:
        if new_id[0] == '.':
            new_id = new_id[1:]
            
    if new_id:
        if new_id[-1] == ".":
            new_id = new_id[:-1]
            
    if new_id == "":
        new_id = "a"
        
    if len(new_id) >= 16:
        new_id = new_id[:15]
        while new_id:
            if new_id[-1] == ".":
                new_id = new_id[:-1]
            else:
                break
                
    if new_id == "":
        new_id = "a"
        
    if len(new_id) <= 2:
        if len(new_id) == 1:
            new_id += new_id[0]
            new_id += new_id[0]
        if len(new_id) == 2:
            new_id += new_id[1]
            
    answer = new_id
    return answer


# 예전 풀이라 살펴보면 조금 더 깔끔하게 만들 수 있을 것 같습니다.