class Prime:

    def __init__(self) -> None:
        self.prime_list = []
        for _ in range(1001):
           self.prime_list.append(True)
        self.prime_list[1] = False

    def is_prime(self, x: int) -> bool:
        if self.prime_list[x]:
            return True
        else:
            return False

    def prime_marker(self, x: int) -> None:
        for i in range(2, x//2+1):
            if x%i == 0:
                return False
        return True

if __name__ == "__main__":
    n = input()
    numbers = map(int, input().split())

    primes = Prime()
    prime_cnt = 0

    for number in numbers:
        if primes.is_prime(number):
            if primes.prime_marker(number):
                prime_cnt += 1
                for m in range(2*number,1001,number):
                    primes.prime_list[m] = False

    print(prime_cnt)
