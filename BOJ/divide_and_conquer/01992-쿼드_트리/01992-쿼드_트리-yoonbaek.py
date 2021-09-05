from sys import stdin

read = stdin.readline


def is_quad(start_x, start_y, end_x, end_y):
    start = video[start_y][start_x]

    for row in range(start_y, end_y):
        for col in range(start_x, end_x):
            if video[row][col] != start:
                return False

    return start+1


def get_quad_tree(start_x, start_y, end_x, end_y):
    check = is_quad(start_x, start_y, end_x, end_y)
    middle_x = (start_x+end_x)//2
    middle_y = (start_y+end_y)//2

    if not check:
        quad_tree.append("(")
        get_quad_tree(start_x, start_y, middle_x, middle_y) # quad 1
        get_quad_tree(middle_x, start_y, end_x, middle_y) # quad 2
        get_quad_tree(start_x, middle_y, middle_x, end_y) # quad 3
        get_quad_tree(middle_x, middle_y, end_x, end_y) # quad 4
        quad_tree.append(")")
    else:
        quad_tree.append(str(check-1))


if __name__ == "__main__":
    N = int(input())
    video = [list(map(int, read().rstrip())) for _ in range(N)]
    # 압축한 텍스트배열
    quad_tree = []

    get_quad_tree(0,0,N,N)
    
    print(*quad_tree, sep = "")

# git commit -m "code: Solve boj 01992 쿼드 트리 (yoonbaek)"