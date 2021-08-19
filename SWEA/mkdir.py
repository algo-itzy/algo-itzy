import os

# ----------------------------------------------------------------------------------
# 풀 문제 카테고리, 문제번호, 문제명 입력

problem = 'L5018-숫자_추가'
path = './linked_list/' + problem
readme = '# L5018 숫자 추가\n파이썬 SW문제해결 기본 - Linked list'

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
md_fid = open(md_path, 'w')
md_fid.write(readme)
md_fid.close()
