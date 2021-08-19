# solved by YoonBaek

def get_puzzle():
    puzzle = [list(map(int, input().split())) for _ in range(9)]
    return puzzle


def check(puzzle_part):
    criterion = set(range(1, 10))
    return criterion == set(puzzle_part)


def check_game(puzzle):
    # 1: row
    for row in range(9):
        if not check(puzzle[row]):
            return 0
    # 2: col
    for col in zip(*puzzle):
        if not check(list(col)):
            return 0
    # 3: 3 by 3 box
    box_idx = [0, 3, 6]
    for col in box_idx:
        for row in box_idx:
            box = []
            for r in range(row, row+3):
                box += puzzle[r][col:col+3]
            if not check(box):
                return 0

    return 1


if __name__ == "__main__":
    T = int(input())
    
    for tc in range(1, T+1):
        puzzle = get_puzzle()

        print(f"#{tc} {check_game(puzzle)}")