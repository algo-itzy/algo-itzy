import re


def solution(new_id):
    answer = ''
    answer = re.sub('[^a-z0-9\-\_\.]', '', new_id.lower())
    answer = re.sub('\.\.+', '.', answer)
    answer = answer.strip('.')
    if answer == '':
        answer = 'a'
    answer = re.sub('\.$', '', answer[:15])
    while len(answer) < 3:
        answer += answer[-1]
    return answer
