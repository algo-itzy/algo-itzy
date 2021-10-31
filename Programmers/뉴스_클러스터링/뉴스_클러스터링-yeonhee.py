from collections import Counter


def solution(str1, str2):

    def get_list(strings):
        strings = strings.upper()
        str_list = []
        for i in range(len(strings)-1):
            tmp = strings[i:i+2]
            if tmp.isalpha():
                str_list.append(tmp)
        return str_list

    list1 = get_list(str1)
    list2 = get_list(str2)

    if not list1 and not list2:
        return 65536

    c1, c2 = Counter(list1), Counter(list2)
    answer = len(list((c1 & c2).elements())) / len(list((c1 | c2).elements())) * 65536
    return int(answer)


print(solution('FRANCE', 'french'))
print(solution('handshake', 'shake hands'))
print(solution('aa1+aa2', 'AAAA12'))
print(solution('E=M*C^2', 'e=m*c^2'))
