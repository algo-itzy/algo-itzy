n, m = map(int, input().split())        # 사이트 주소의 수 n, 비밀번호 주소의 수 m

dic = {}
for i in range(n):
    site, password = map(str, input().split())
    dic[site] = password

for i in range(m):                      # 사이트에 해당되는 비밀번호 출력하기
    site_find = input()
    print(

# git commit -m "code: Solve boj 17219 비밀번호 찾기 (yeonju)"