# solved by YoonBaek

if __name__ == "__main__":
    T = int(input())

    for tc in range(1, T+1):
        str1 = set(input())
        str2 = input()

        max_cnt = 0
        for char1 in str1:
            cnt = 0
            for char2 in str2:
                if char1 == char2:
                    cnt += 1

            max_cnt = max(max_cnt, cnt)
        
        print(f"#{tc} {max_cnt}")