# 알고있지! (Algo-Itzy)

<br>

## 📋 스터디 계획

- **인원** : [위연주](https://github.com/Julia-we-s2), [백승윤](https://github.com/YoonBaek), [채연희](https://github.com/hing9u), [소석진](https://github.com/seokzin), [김승규](https://github.com/ed-kyu)(백준 그룹 관리), [정지웅](https://github.com/JiWoongJeong)(총무), [한승주](https://github.com/chaselover)
- **문제 수준** : solved.ac - 문제 - CLASS에서 모임 때마다 다음 문제 선정

- **모임 요일 및 시간** : 목요일 20시 / 일요일 12시 (2시간 / 유동적)
    - 파트 별 담당자 선정, 담당자가 파트 내 모든 코드 리뷰
    - 새로운 개념 (알고리즘) 등장 시 간단한 설명 추가 (시각적 자료가 있으면 👍)

- 코드 제출은 모임 **1시간 전**까지
    1. [BOJ 그룹](https://www.acmicpc.net/group/11918) - 연습 : **스코어보드 업데이트** ⭐
    2. **저장소에 코드 업로드**
        ```
        - 문제를 못 풀었을 경우, 문제에 대한 해석 및 해당 알고리즘 공부 내용을 주석으로 최대한 적어서 업로드하기
        - 그리고 다음 스터디 전까지 재풀이해서 올리기
        
        → 지키지 않을 시, 문제를 안 푼 것으로 간주하여 벌금 부과합니다!
        ```

- **소통 채널**
    - [**Discord**](https://discord.gg/CTNYwBW8) : 주 소통 채널
    - [**Github**](https://github.com/ss6-algorithm-study/algo-itzy) : 코드 업로드 및 버전 관리
    - [**BOJ 그룹**](https://www.acmicpc.net/group/11918) : 문제 리스트 제공 및 코드 제출 - 스코어보드 기록
    - [**Notion**](https://www.notion.so/Algo-Itzy-ca5f3350ae5e42cdb487549170fa6f09) : 문제 리스트 정리 (카테고리 및 티어 참고) / 벌금 내역 관리
    - **카카오톡** : 카카오페이 / 긴급 공지 및 연락



<br>

## 📜 Convention

### 1. **Code Convention**

- 코드마다 주석 달기
- 변수와 함수 이름은 어떤 역할을 하는지 알 수 있도록 붙이기



<br>

### 2. **Commit Convention**

- **commit 분리하기**
  - 한번에 `git add .`를 지양합니다.
  - 문제별, 타입별로 commit을 분리해서 작성합니다.
- 제목 첫 글자는 `대문자`
  - ex: `fix: Change input() to readline()`
- 요소 간 구분은 `-` (hyphen), 요소 내 공백은 `_` (underbar)

```
- code  : 코드를 제출할 때
- fix   : 코드를 수정할 때 (틀린 문제를 맞게 만들었을 때)
- docs  : README를 수정했을 때
- refac : 맞은 문제를 개선했을 때
- chore : 그 외 자잘한 수정(디렉토리 추가..)

--------------------------------------------------------------------------

$ git add 10094-에라스토스의_체-kimssafy.py
$ git commit -m "code: Solve 문제플랫폼 문제번호 문제이름 (작성자)"
$ git commit -m "fix: 뭐했는지 (작성자)"

(예시)
$ git commit -m "code: Solve boj 10972 에라스토스의 체 (소석진)"
$ git commit -m "fix: Change input() to readline()"
```

- 일단 각자 푸쉬 → ⭐ **push 전에 pull 필수!!!** ⭐



<br>

### 3. Github 폴더

![image](https://user-images.githubusercontent.com/87457066/128278963-21470384-3c70-450d-936c-5b3e34723f78.png)

```
ss6-algorithm-study/algo-itzy
├──BOJ
│   ├──0-1_bfs(너비 우선 탐색)	
│   ├──arbitrary_precision / big integers (임의 정밀도 / 큰 수 연산)	
│   ├──area_of_a_polygon (다각형의 넓이)	
│   ├──arithmetic (사칙연산)	
│   ├──backtracking (백트래킹)	
│   ├──bellman–ford (벨만–포드)	
│   ├──binary_search (이분 탐색)	
│   ├──bfs (너비 우선 탐색)	
│   ├──bruteforcing (브루트포스 알고리즘)	
│   ├──combinatorics (조합론)	
│   ├──data_structure (자료 구조)	
│   ├──deque (덱)	
│   ├──dfs (깊이 우선 탐색)	
│   ├──dijkstra (다익스트라)	
│   ├──divide_and_conquer (분할 정복)	
│   ├──dp (다이나믹 프로그래밍)
│   │   ├──01003-피보나치_함수
│   │   │   ├──01003-피보나치_함수-각자id.py
│   │   │   ├── ...
│   │   │   └── README.md
│   │   └──09461-파도반_수열
│   │       ├──09461-파도반_수열-각자id.py
│   │       ├── ...
│   │       └── README.md
│   ├──exponentiation_by_squaring (분할 정복을 이용한 거듭제곱)	
│   ├──floyd–warshall (플로이드–와샬)	
│   ├──geometry (기하학)	
│   ├──graph_theory (그래프 이론)	
│   ├──graph_traversal (그래프 탐색)	
│   ├──greedy (그리디 알고리즘)	
│   ├──implementation (구현)	
│   ├──knapsack (배낭 문제)	
│   ├──mathematics (수학)	
│   ├──number_theory (정수론)	
│   ├──prefix_sum (누적 합)	
│   ├──primality_test (소수 판정)	
│   ├──priority_queue (우선순위 큐)	
│   ├──queue (큐)	
│   ├──recursion (재귀)	
│   ├──set-map_by_hashing (해시를 사용한 집합과 맵)	
│   ├──set-map_by_trees (트리를 사용한 집합과 맵)	
│   ├──sieve_of_eratosthenes (에라토스테네스의 체)	
│   ├──sorting (정렬)	
│   ├──stack (스택)	
│   ├──string (문자열)	
│   ├──topological_sorting (위상 정렬)	
│   ├──tree (트리)	
│   ├──two-pointer (투 포인터)	
│   └──value-coordinate_compression (값 / 좌표 압축)
├──SWEA
├──Programmers
└──README.md
```



<br>

## 🙆 **참가자들 알고리즘 경험도**

- [위연주](https://github.com/Julia-we-s2)  : 프로그래머스 문제 유형별 1, 2 푸셨었음. 파이썬 잘 모름 열심히 할게요😭
- [채연희](https://github.com/hing9u)  : 백준 단계 초반 30제 + 해커랭크 easy ~ medium
- [백승윤](https://github.com/YoonBaek)  : 거의 백준만. 파이썬 경험 적음. BOJ S2 (Golang)
- [김승규](https://github.com/ed-kyu)  : 백준 실버 초급 단계정도
- [소석진](https://github.com/seokzin)  : 백준 골드3
- [정지웅](https://github.com/JiWoongJeong)  : 경험 없습니다 열심히 해볼게요
- [한승주](https://github.com/chaselover)  : 백준 플래티넘 ㄷㄷ



<br>

## 💰 스터디 효율성을 위한 벌금

    ~~ 사채업자 아니에요 우리의 실력 향상을 위한 방침입니다 ^_^ 돈 많이내면 땡큐. 잦은 지각과 결석 바랍니다 ~~

- 스터디 결석 시 : 6,000원
    - 사유 결석 : 누가 들어도 합당한 사유 — 면제
- 스터디 정시 지각 시 : 4,000원
- 문제 안 풀었을 시 (모임 1시간 전까지) : 한 문제 당 2,000원

<br>

- 벌금 사용처 : 코로나 잠잠해지면 오프라인 회식 때 **FLEX**
- 총무에게 다음날 낮 12시 전까지 카카오 페이로 입금 (제 시간 내에 미입금 시 추가 1,000원)
- 벌금 내역 : Notion에서 관리
