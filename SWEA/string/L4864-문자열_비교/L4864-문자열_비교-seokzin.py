T = int(input())

for tc in range(1, T+1):
    str1 = input()  # short str
    str2 = input()  # long str
    
    print(f"#{tc}", 1 if str2.find(str1) > 0 else 0)