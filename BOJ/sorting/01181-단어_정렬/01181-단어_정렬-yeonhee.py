# 데이터 입력 및 중복 제거
words = list(set([input() for _ in range(int(input()))]))
# 길이 -> 사전 순 정렬 및 출력
print('\n'.join(sorted(words, key = lambda x: (len(x), x))))

'''
숏코딩으로 해봤어요 :)
'''