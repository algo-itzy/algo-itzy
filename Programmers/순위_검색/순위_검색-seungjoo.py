# git commit -m "code: Solve programmers 순위 검색 (seungjoo)"
from collections import defaultdict
from bisect import bisect_left

def solution(info, query):
    score_set = defaultdict(list)
    answer = []    
    for each in info:
        lang, job, stat, food, score = each.split()
        for l in (lang, '-'):
            for j in (job, '-'):
                for s in (stat, '-'):
                    for f in (food, '-'):
                        score_set[(l, j, s, f)] += [int(score)]
        
    for value in score_set.values(): 
        value.sort()
    
    for each in query:
        lang, job, stat, last = each.split(' and ')
        food, score = last.split()
        target_set = score_set[(lang, job, stat, food)]
        index = bisect_left(target_set, int(score))
        answer.append(len(target_set) - index)
        
    return answer

# def solution(info, query):
#     answer = []
#     lang_set = defaultdict(set)
#     job_set = defaultdict(set)
#     stat_set = defaultdict(set)
#     food_set = defaultdict(set)
#     score_set = {}
#     for idx, each in enumerate(info):
#         lang, job, stat, food, score = each.split()
#         lang_set[lang].add(idx)
#         job_set[job].add(idx)
#         stat_set[stat].add(idx)
#         food_set[food].add(idx)
#         score_set[idx] = int(score)
#     for each in query:
#         lang, job, stat, last = each.split(' and ')
#         food, score = last.split()
#         pivot = set([i for i in range(len(info))])
#         if lang != '-':
#             pivot &= lang_set[lang]
#         if job != '-':
#             pivot &= job_set[job]
#         if stat != '-':
#             pivot &= stat_set[stat]
#         if food != '-':
#             pivot &= food_set[food]
#         tmp = sorted([score_set[idx] for idx in pivot])
#         left = bisect_left(tmp, int(score))
#         answer.append(len(tmp) - left)
#     return answer
    