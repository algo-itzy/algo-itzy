# 2단계
def check_valid_chars(id):
    valid_id = ''
    
    for char in id:
        if char in valid_set:
            valid_id += char

    return valid_id

# 3단계
def check_duple_commas(id):
    checked_id = ''
    flag = True

    for char in id:
        if char == "." and not flag:
            continue
        else:
            checked_id += char
            if char == ".":
                flag = False
            else:
                flag = True
        
    return checked_id

# 7단계
def check_length(id):
    if len(id) <= 2:
        last = id[-1]
        while len(id) < 3:
            id += last

    return id


def solution(new_id):
    # 1
    corrected = new_id.lower()
    # 2
    corrected = check_valid_chars(corrected)
    # 3
    corrected = check_duple_commas(corrected)
    # 4
    corrected = corrected.strip('.')
    # 5
    if not corrected:
        corrected = "a"
    # 6
    corrected = corrected[:15].rstrip('.')
    # 7
    corrected = check_length(corrected)
    answer = corrected
    return answer


if __name__ == "__main__":
    new_id = input()
    valid_chars = 'abcdefghijklmnopqrstuvwxyz1234567890-_.'
    valid_set = set()
    
    for char in valid_chars:
        valid_set.add(char)

    ans = solution(new_id)
    
    print(ans)

# git commit -m "code: Solve programmers 신규 아이디 추천 (yoonbaek)"