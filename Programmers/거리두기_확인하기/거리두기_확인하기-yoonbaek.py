from collections import deque
SIZE = 5
MOVES = ((-1, 0), (1, 0), (0, -1), (0, 1))


def solution(places):
    visited = set()

    class Location():
        def __init__(self, row, col, dist=0):
            self.row, self.col, self.dist = row, col, dist

        def is_person(self):
            return place[self.row][self.col] == "P"

        def is_empty(self):
            return place[self.row][self.col] == "O"


    def recover():
        while visited:
            visited.pop()
            

    def search(start_loc):
        q = deque([start_loc])
        visited.add((start_loc.row, start_loc.col))

        try:
            while q:
                now = q.popleft()

                for y, x in MOVES:
                    y, x = y+now.row, x+now.col
                    if 0 <= x < SIZE and 0 <= y < SIZE and (y, x) not in visited:
                        next = Location(y, x, now.dist+1)
                        if next.is_person():
                            if next.dist <= 2:
                                return 0
                        if next.is_empty():
                            visited.add((y, x))
                            q.append(next)
            return 1

        finally:
            recover()


    answers = []
    for place in places:
        starts = [Location(row, col, 0) for col in range(SIZE) for row in range(SIZE)]
        starts = filter(lambda x: x.is_person(), starts)

        for start in starts:
            if not search(start):
                answers.append(0)
                break
        else:
            answers.append(1)  

    return answers

# git commit -m "code: Solve programmers 거리두기 확인하기 (yoonbaek)"