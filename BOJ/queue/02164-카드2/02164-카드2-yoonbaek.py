# solved by YoonBaek
"""
이런 풀이도 시간초과 안되고 풀린다는 것만 알고 넘어가세요
성능은 popleft가 사기적으로 좋습니다
빌트인 타입 클래스들로는 쉽게 풀 수 없는 문제였습니다.
"""

class Queue:

    def __init__(self, items: list):
        self.item = items
        self.size = len(items)
        # 밀어내기 싫어서 구현하는 pop_cnt
        self.pop_cnt = -1

    def push(self, elem: str):
        self.item.append(elem)
        self.size+=1
    
    def pop(self) -> str:
        # pop_cnt를 통해 리스트 중간에 있지만 리스트 처음인 것 처럼 위장.
        self.pop_cnt+=1
        return self.item[self.pop_cnt]

if __name__ == "__main__":
    n = int(input())
    cards = Queue(list(range(1,n+1)))

    # solve
    while True:
        cards.pop()
        if cards.size == 2*n - 1:
            print(cards.item[-1])
            break

        cards.push(cards.pop())
    