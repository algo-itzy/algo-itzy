# linked list 연습
# 내장 insert 절실
class Node:
    def __init__(self, item):
        self.prev = None
        self.item = item
        self.next = None
    

class LinkedList:
    def __init__(self):
        self.head = Node(None)
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


    def insert(self, index, item):
        node = Node(item)

        if not self.size:
            self.head = node
            self.tail = node

        elif self.size <= index:
            self.append(node)

        elif not index:
            self.head.prev = node
            node.next = self.head
            self.head = node

        else:
            from_tail = self.size - index
            if from_tail > index:
                now = self.head
                for _ in range(index):
                    now = now.next
            else:
                now = self.tail
                for _ in range(from_tail-1):
                    now = now.prev

            now.prev.next = node
            node.prev = now.prev
            node.next = now
            now.prev = node
        
        self.size+=1


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
        N, M, L = map(int, input().split())
        nums = list(map(int, input().split()))

        linked_list = LinkedList()

        for num in nums:
            linked_list.append(num)

        for _ in range(M):
            idx, val = map(int, input().split())
            linked_list.insert(idx, val)
        
        print(f"#{tc} {linked_list.get(L)}")
