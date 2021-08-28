import os

# ----------------------------------------------------------------------------------
print('------------------------------------------------------------')
print('노션 테이블의 [문제번호][문제 이름][알고리즘 분류]를 복붙해주세요')
print('------------------------------------------------------------')

datas = []

for _ in range(7):  # 7문제로 고정했습니다. 추후 리팩토링
    datas.append(input().split())

for data in datas:
    num = data.pop(0).zfill(5)
    category = data.pop()
    title = ' '.join(data)
    title_bar = title.replace(' ', '_')

    problem = f'{num}-{title_bar}'
    path = f'./{category}/{problem}' 

    readme = f"# {str(int(num))} {title}\nhttps://www.acmicpc.net/problem/{num}"

# ----------------------------------------------------------------------------------

    # 디렉토리 생성
    if not os.path.exists(path):
        os.makedirs(path)
        # 개별 파일 생성
        members = ['jiwoong', 'seokzin', 'seungjoo', 'seungkyu', 'yeonhee', 'yeonju', 'yoonbaek']

        for member in members:
            filepath = os.path.join(path, f'{problem}-{member}.py')
            fid = open(filepath, 'w', encoding='utf8')
            fid.write(f'# git commit -m "code: Solve boj {num} {title} ({member})"')
            fid.close()

        # README 생성
        md_path = os.path.join(path, 'README.md')
        md_fid = open(md_path, 'w', encoding='utf8')
        md_fid.write(readme)
        md_fid.close()

        print(f'{num} 디렉토리 생성 끝!')

    else:
        print(f'{num} 이미 존재하는 디렉토리입니다.')
