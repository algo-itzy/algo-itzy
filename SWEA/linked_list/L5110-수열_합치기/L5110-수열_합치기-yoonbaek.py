# linked list 연습
# 못 풀었습니다.
intput = lambda : map(int, input().split())


class Node:
    def __init__(self, item):
        self.prev = None
        self.item = item
        self.next = None
    

class LinkedList:
    def __init__(self):
        self.head = Node(None)
        self.past = None
        self.now = None
        self.tail = Node(None)
        self.size = 0

    
    def append(self, item):
        node = Node(item)

        if self.size:
            self.tail.next = node
            node.prev = self.tail

        else:
            self.head = node

        self.tail = node
        self.size += 1


    def list_to_ll(self, nums: list):
        for num in nums:
            self.append(num)

    
    def front(self):
        if not self.size:
            return
        self.past = self.head
        self.now = self.head.next
        return self.now.item

    def go(self):
        self.past = self.now
        self.now = self.now.next
        if not self.now:
            return
        return self.now.item

    def insert_ll(self, compare: int, ll):
        self.now = self.head

        now_front = self.front()
        for _ in range(self.size):
            if now_front > compare:
                self.past.next = ll.head.next
                ll.tail.link = self.now
                self.size+=ll.size
                break
            now_front = self.go()
        else:
            self.tail.next = ll.head.link
            self.size += ll.size

    def get(self, index):
        if not self.size:
            return None
        if index >= self.size:
            return self.tail.item
        
        from_tail = self.size - index
        if from_tail > index:
            now = self.head
            for _ in range(index):
                now = now.next
        
        else:
            now = self.tail
            for _ in range(from_tail-1):
                now = now.prev
        
        return now.item


if __name__ == "__main__":
    T = int(input())

    for tc in range(1, T+1):
        N, M = intput()
        LL1 = LinkedList()

        nums = list(intput())
        LL1.list_to_ll(nums)
        
        for _ in range(M-1):
            nums = list(intput())
            compare = nums[0]
            LL2 = LinkedList()

            nums = list(intput())
            LL2.list_to_ll(nums)

            LL1.insert_ll(compare, LL2)

        result = []
        for i in range(LL1.size-1, LL1.size-11, -1):
            result.apppend(LL1.get(i))

        ans = "".join(result)
        print(f"#{tc} {ans}")


            