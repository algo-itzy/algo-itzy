# solved by YoonBaek
# 보이어 무어 법칙 구현 연습
# 파이썬은 이미 string.find로 구현 돼 있습니다.
# 추후 보강하겠습니다.

# def skip():
#     pass


# def BM_find(target: str, source: str) -> int:
#     t_len = len(target)
#     s_len = len(source)

#     s_idx = 0
#     while s_idx < s_len-t_len+1:
#         compare = source[s_idx:s_idx+t_len]

#         # 첫 글자 일치하면 시작
#         if compare[0] == target[0]:
#             for c_idx in range(t_len-1, 0, -1):
#                 if compare[c_idx] != target[c_idx]:
#                     s_idx += t_len-c_idx
#                     break
#                 if c_idx == 1:
#                     return 1
#         else:
#             s_idx += 1
#     return 0


if __name__ == "__main__":
    T = int(input())
    
    for tc in range(1, T+1):
        target = input() # str1
        source = input() # str2

        # if not str.find() == -1, print 1
        print(f"#{tc} {1 if source.find(target) > 0 else 0}")