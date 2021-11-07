def solution(files):
    rearranged = []
    head, tmp, number, tail = '', '', '', ''

    for file in files:
        for j in range(len(file)):
            if file[j].isdigit():
                head += file[:j]
                tmp += file[j:]
                break

        for i in range(len(tmp)):
            if tmp[i].isdigit() and i < 5: # number 는 최대 5글자의 숫자
                number += tmp[i]
            else:
                tail += tmp[i:]
                break

        rearranged.append([head, number, tail])
        head, tmp, number, tail = '', '', '', ''

    rearranged = sorted(rearranged, key=lambda x: (x[0].lower(), int(x[1])))

    return([''.join(i) for i in rearranged])


# solution(['img234544'])
# print(solution(['img3','img44','img31','img10','img33']))
# print(solution(["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]))
print(solution(["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"]))

# git commit -m "code: Solve programmers 파일명 정렬 (yeonju)"