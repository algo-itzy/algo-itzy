# git commit -m "code: Solve programmers 문자열 압축 (jiwoong)"
def solution(s):
    ans = [len(s)]
    for i in range(1, len(s)):
        word = ""
        arr = [s[j:j + i] for j in range(0, len(s), i)]
        stack = [[arr[0], 1]]

        for k in arr[1:]:
            if stack[-1][0] != k:
                stack.append([k, 1])
            else:
                stack[-1][1] += 1
        word += ''.join([str(cnt) + word if cnt > 1 else word for word, cnt in stack])
        ans.append(len(word))
    print(ans)
    return min(ans)
