# git commit -m "code: Solve programmers 신규 아이디 추천 (seungjoo)"
def solution(new_id):
    answer = ''
    for char in new_id:
        if char.isalpha():
            answer += char.lower()
        elif char == '.' and answer and answer[-1] != '.':
            answer += '.'
        elif char.isdigit() or char in '-_':
            answer += char
    if not answer:
        answer += 'a'
    elif len(answer) > 15:
        answer = answer[:15]
    if answer[-1] == '.':
        answer = answer[:-1]
    while len(answer) < 3:
        answer = answer + answer[-1]
    return answer