t =int(input())

for tc in range(t):
    n, m = map(int, input().split()) # 맨 앞의 원소를 맨뒤로 보내는 걸 m 번 만큼
    
    li = list(map(int, input().split()))

    final = m % n                   # n = 3, m = 10 인 경우, 3번째 6번째 9번째가 처음 입력받았던 리스트 순서대로 다시 반복된다는 것을 이용
                                    # 나머지 값이 앞에서부터 제껴줘야 할 원소 개수
                                    # 그렇다면 위 예시의 경우 3번째 원소가 문제의 답이 되는데, 2번째 인덱스이기에 final의 위치 그대로가 답이 됨 
    ans =li[final] 

    print(f'#{tc+1} {ans}')