# git commit -m "code: Solve programmers 파일명 정렬 (jiwoong)"
def solution(files):
    answer = []
    arr = []
    nums = "0123456789"
    for i, file in enumerate(files):
        check = "h"
        h = n = ""
        for f in file:
            if check == "h" and f not in nums:
                h += f
            elif check == "h" and f in nums:
                check = "n"
                n += f
            elif check == "n" and f in nums and len(n) < 5:
                n += f
            elif check == "n" and (f not in nums or len(n) >= 5):
                check = "t"
        arr.append((file, h.lower(), int(n)))
    arr.sort(key=lambda x: (x[1], x[2]))  # head, number 기준 정렬
    answer = [file[0] for file in arr]
    return answer
