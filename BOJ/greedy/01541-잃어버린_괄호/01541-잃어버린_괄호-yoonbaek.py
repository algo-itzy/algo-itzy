# 잃어버린 괄호
# 플러스 끼리 묶어서 더한 값을 죄다 빼기만 하면 결과가 나오는 문제였습니다.

if __name__ == "__main__":
    note = input()
    exprs = note.split("-")
    length = len(exprs)

    minimum = 0
    for i in range(length):
        exprs[i] = sum(map(int, exprs[i].split("+")))
        if i == 0:
            minimum = exprs[i]
        else:
            minimum -= exprs[i]

    print(minimum)    


# git commit -m "code: Solve boj 01541 잃어버린 괄호 (yoonbaek)"