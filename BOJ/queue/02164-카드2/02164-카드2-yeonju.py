from collections import deque 

N = int(input()) 
deque = deque([i for i in range(1, N+1)]) #  1부터 N까지 숫자들 덱에 담기

while len(deque) > 1: 
    deque.popleft() # 맨 앞의 카드는 버리기
    first = deque.popleft() # 그 다음으로 맨 우에 오는 카드를 빼서, 맨 뒤로 추가
    deque.append(first) 
    
print(deque[0])


"""
deque 의 메서드:

deque.append(item): item을 데크의 오른쪽 끝에 삽입한다.
deque.appendleft(item): item을 데크의 왼쪽 끝에 삽입한다.
deque.pop(): 데크의 오른쪽 끝 엘리먼트를 가져오는 동시에 데크에서 삭제한다.
deque.popleft(): 데크의 왼쪽 끝 엘리먼트를 가져오는 동시에 데크에서 삭제한다.
deque.extend(array): 주어진 배열(array)을 순환하면서 데크의 오른쪽에 추가한다.
deque.extendleft(array): 주어진 배열(array)을 순환하면서 데크의 왼쪽에 추가한다.
deque.remove(item): item을 데크에서 찾아 삭제한다.
deque.rotate(num): 데크를 num만큼 회전한다(양수면 오른쪽, 음수면 왼쪽)



이렇게 풀면 시간 초과 뜸

N = int(input())
list = [i for i in range(1,(N+1))]

while len(list) > 1:
    list.pop(0)

    first = list[0]
    
    list.append(first) 
    list.pop(0)

print(list[0])
"""
    

