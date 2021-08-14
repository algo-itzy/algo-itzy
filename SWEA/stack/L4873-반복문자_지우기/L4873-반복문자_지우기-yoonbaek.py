# solved by YoonBaek

if __name__ == "__main__":
    T = int(input())

    for tc in range(1, T+1):
        target = input()
        stack = []

        for char in target:
            if stack:
                if char == stack[-1]:
                    stack.pop()
                    continue

            stack.append(char)

        print(f"#{tc} {len(stack)}")