# solved by YoonBaek
class PStack: # 괄호 스택

    def __init__(self):
        self.items = []
        self.size = 0

    def ppush(self, x):
        if x == "{" or x == "(":
            self.items.append(x)
    
    def ppop(self):
        return self.items.pop()

    def is_vps(self, x):
        if x == "}" or x == ")":
            if self.items:
                pop = self.ppop()
                if x == "}":
                    if pop != "{":
                        return 0
                elif x == ")":
                    if pop != "(":
                        return 0
            else:
                return 0
                
        return 1


if __name__ == "__main__":
    T = int(input())
    
    for tc in range(1, T+1):
        line = input()
        stack = PStack()

        is_vps = 1
        for char in line:
            stack.ppush(char)

            is_vps = stack.is_vps(char)
            if not is_vps:
                break

        print(f"#{tc}", is_vps if not stack.items else 0)
        
        