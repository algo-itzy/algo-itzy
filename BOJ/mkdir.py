import os

# ----------------------------------------------------------------------------------
# 풀 문제 카테고리, 문제번호, 문제명 입력

problem = '07576-토마토'
path = './bfs/' + problem
readme = '# 7576 토마토\nhttps://www.acmicpc.net/problem/7576'

"""
요소 간 구분은 - (hyphen), 요소 내 공백은 _ (underbar) 지켜서 입력해주세요.
boj 문제 중 문제번호가 4자리인 경우 앞에 0을 붙여주세요.

예시 ) bfs/07576-토마토
"""

# ----------------------------------------------------------------------------------

# 디렉토리 생성
try:
    if not os.path.exists(path):
        os.makedirs(path)
except OSError:
    print('이미 존재하는 디렉토리입니다.')

# 개별 파일 생성
members = ['jiwoong', 'seokzin', 'seungjoo', 'seungkyu', 'yeonhee', 'yeonju', 'yoonbaek']

for member in members:
    filepath = os.path.join(path, f'{problem}-{member}.py')
    fid = open(filepath, 'w')
    fid.write('# delete this and solve here')
    fid.close()

# README 생성
md_path = os.path.join(path, 'README.md')
md_fid = open(md_path, 'w', encoding='utf8')
md_fid.write(readme)
md_fid.close()
