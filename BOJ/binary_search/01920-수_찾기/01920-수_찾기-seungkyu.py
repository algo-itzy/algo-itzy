'''
시간 초과나지 않도록 이분 탐색 이용
이분 탐색 => O(log(N))
1. 정렬
2. left, right 설정
3. mid 값(인덱스가 (left + right) / 2)과 비교
4. left, right 바꿔서 반복
'''
import sys

def input_func() :
    input = sys.stdin.readline
    n = int(input())
    a_numbers = list(map(int, input().rstrip().split()))
    m = int(input())
    check_numbers = list(map(int, input().rstrip().split()))

    a_numbers.sort() # 이분 탐색에서는 탐색할 대상이 정렬되어 있어야 함
    return a_numbers, check_numbers

def binary_search(a_numbers, check_numbers) :

    for number in check_numbers :
        flag = False # flag 변수 for문 바깥에 선언하면 안됨
        left = 0
        right = len(a_numbers) - 1

        while (left <= right) :
            mid = (left + right) // 2 # left, right값이 바뀌었으므로 값 업데이트
            if a_numbers[mid] > number : # number가 left ~ mid 사이에 존재
                right = mid - 1
            elif a_numbers[mid] < number : # number가 mid ~ right 사이에 존재
                left = mid + 1
            else :
                flag = True
                break

        print(1) if flag == True else print(0)


if __name__ == '__main__' :
    a_numbers, check_numbers = input_func()
    binary_search(a_numbers, check_numbers)
