class Prime:
    """
    Prime을 다루는 클래스입니다.
    """

    def __init__(self) -> None:
        # 프라임 여부를 저장하는 prime_list를 생성합니다.
        # 문제 조건 상 1000개 이내의 정수에 대해 질문하기 때문에 range(1000 + 1)을 사용합니다.
        # 1을 더한 이유는 편하게 인덱스에 정수 그 자체를 넣기 위함입니다.
        self.prime_list = []

        for _ in range(1001):
           # False인 경우를 체크하는 로직을 구성했기 때문에 디폴트는 True로 설정합니다.
           self.prime_list.append(True)
        # 1은 소수가 아니기 때문에 False로 고정합니다.
        self.prime_list[1] = False

    def is_prime(self, x: int) -> bool:
        # 숫자를 받고 prime인지 여부를 리턴하는 함수입니다.
        # 리스트에 저장된 bool 값을 출력
        return self.prime_list[x]

    def check_prime(self, x: int) -> None:
        # prime 여부 업데이트
        for i in range(2, x//2+1):
            # prime이 0이면 false를 리턴하고 종료
            if not x%i:
                return False
        return True

if __name__ == "__main__":
    n = input()
    numbers = map(int, input().split())

    primes = Prime()
    prime_cnt = 0
    # solve
    for number in numbers:
        # 메서드 내부 리스트에 저장된 값부터 체크
        if primes.is_prime(number):
            # True일 때 실제로 True가 맞는지 한 번 더 체크
            if primes.check_prime(number):
                # True 라는 결론이 나오면, 카운트를 올림
                prime_cnt += 1
                # 소수의 배수들은 절대 소수일 수 없으므로
                # 두 번 다시 체크할 필요 없게 False값을 리스트 내부 저장소에 저장
                for m in range(2*number, 1001, number):
                    primes.prime_list[m] = False
    # cnt를 반환
    print(prime_cnt)
