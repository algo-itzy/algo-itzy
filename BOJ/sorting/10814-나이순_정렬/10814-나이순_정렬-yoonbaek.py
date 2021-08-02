# solved by Yoon Baek
from sys import stdin, stdout

input, print = stdin.readline, stdout.write

# save
def save() -> None:
    age, name = input().split()
    # save name at AGEth list
    ages[int(age)].append(name)

if __name__ == "__main__":
    # generate list to save data
    ages = []
    # make 200 (age range) level2 lists
    for _ in range(201): ages+=[[]]

    n = int(input())
    for _ in range(n): save()

    # untie
    for age, names in enumerate(ages):
        for name in names:
            print(f"{age} {name}\n")