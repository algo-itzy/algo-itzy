import sys
n = int(input())

# 들어오는 수열 저장하는 리스트
numbers = []
for _ in range(n):
    number = int(sys.stdin.readline())
    numbers.append(number)

# 숫자를 저장했다 뺏다 하는 스택 새로 만듬
stack = []
# +, - 값 저장할 리스트
answer = []

for i in range(1, n+1):
    # 스택에 숫자 오름차순으로 저장하기 위해 1부터 n까지 숫자 범위를 설정
    answer.append('+')
    stack.append(i)
    # 수열의 첫 번째 수가 제일 먼저 나타나는 수이므로 스택에 제일 위에 있다면 빼기
    # 단, 뺀 후에 계속해서 수열 제일 앞의 값(update된)과 스택 제일 위 값이 계속 같을 수 있으므로 while 이용
    while stack[-1] == numbers[0]:
        answer.append('-')
        stack.pop()
        # 수열 제일 앞 수 update 위해 remove 활용 --> 작동 시간이 길어지므로 보완해보려고 함.
        numbers.remove(numbers[0])
        # 스택이 비었다는 것은 모든 숫자를 활용한 것이고, 수열을 완성한 것이므로 break 후 답 출력
        if stack == []:
            break

if stack == []:
    print(*answer, sep='\n')
else:
    print('NO')
