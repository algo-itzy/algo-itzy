# solved by YoonBaek
from sys import stdin

class Memory:
    """
    sorting memory
    이거 무슨 기법이더라
    아무튼 저장할 때마다 글자 수대로 정렬
    """

    def __init__(self, n=51) -> None:
        # memory : 2d list
        self.memory = []
        # given condition : length < 51 
        for _ in range(n):
            self.memory += [[]]
    
    def save(self, word: str) -> None:
        # save words in lists by length
        self.memory[len(word)].append(word)

    def print_by_order(self) -> None:
        prev = ""
        for words in self.memory:
            # sort in same length words.
            words.sort()
            for word in words:
                # ignore duplicates
                if prev != word:
                    print(word) 
                    prev=word

if __name__ == "__main__":
    words = stdin.read().rstrip().split("\n")[1:]
    memory = Memory()

    # save and sort
    for word in words:
        memory.save(word)
    
    # print in order
    memory.print_by_order()
