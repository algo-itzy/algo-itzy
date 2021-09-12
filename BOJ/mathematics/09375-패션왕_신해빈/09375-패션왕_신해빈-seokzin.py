for _ in range(int(input())):
    dic = {}
    res = 1
    
    for _ in range(int(input())):
        name, type = input().split()
        
        if type in dic.keys():
            dic[type] += 1
        else:
            dic[type] = 2  # 좋은 방법은 아닌데 2로 초기화
        
    for key in dic.keys():
        res *= dic[key]

    print(res-1)