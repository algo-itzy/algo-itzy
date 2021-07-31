'''
한쪽에서 빼서 반대쪽으로 값을 집어넣은 작업이 있으므로 큐 이용
'''
from collections import deque

def solve() :
    n = int(input())
    card_que = deque()
    card_que.extend([i for i in range(1,n+1)])

    while 1 :

        if len(card_que) == 1 : # 남은 카드 1개일 때 반복문 종료
            ans = card_que.pop()
            print(ans)
            break
        
        card_que.popleft() # 제일 위의 수 버리기

        # 이 자리에 if문 넣으려고 했는데, n = 1일때 성립하지 않는다는 문제가 있다.    

        to_end_num = card_que.popleft() # 제일 위의 수 
        card_que.append(to_end_num) # 맨 뒤로 보내기

if __name__ == '__main__' :
    solve()
