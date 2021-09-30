def is_run(arr, index):
    if index < 8 and arr[index+1] and arr[index+2]:
        return True
    if 0 < index < 8 and arr[index-1] and arr[index+1]:
        return True
    if index > 1 and arr[index-2] and arr[index-1]:
        return True
    return False


def is_triplet(val):
    if val == 3:
        return True
    return False


if __name__ == "__main__":
    T = int(input())

    for tc in range(1, T+1):
        game = list(map(int, input().split()))

        player1 = game[::2]
        visited1 = [0] * 10

        player2 = game[1::2]
        visited2 = [0] * 10

        res = 0

        for i in range(6):
            card1 = player1[i]; card2 = player2[i]
            visited1[card1] += 1
            visited2[card2] += 1

            if is_run(visited1, card1) or is_triplet(visited1[card1]):
                res = 1
                break
            elif is_run(visited2, card2) or is_triplet(visited2[card2]):
                res = 2
                break

        print(f"#{tc} {res}")

        
 # git commit -m "code: Solve swea L5203 베이비진 게임 (yoonbaek)"