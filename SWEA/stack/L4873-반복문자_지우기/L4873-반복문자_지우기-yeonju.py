t = int(input())

for tc in range(t):
    st = input()
    
    li =[] 

    for i in st:
        if li and i == li[-1]:  # 담겨있는 문자와 담으려는 문자가 같으면 제거
            li.pop()
        else:
            li.append(i)
            


  
    print(f'#{tc+1} {len(li)}'}

   