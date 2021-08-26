# solved by YoonBaek


def permutation_pruning(i, cur_min):
    global global_min

    # pruning
    if cur_min > global_min:
        return

    if i == N:
        global_min = min(global_min, cur_min)  
    
    for j in range(N): 
        if not visited[j]:
            visited[j] = 1
            permutation_pruning(i+1, cur_min+mat[i][j])
            visited[j] = 0
    

if __name__ == "__main__":
    tc = int(input())

    for T in range(1, tc+1):
        N = int(input())
        
        mat = [list(map(int, input().split())) for _ in range(N)]
        
        # 10보다 작은 자연수 N개라고 했음
        global_min = N * 9
        visited = [0] * N

        permutation_pruning(0, 0)
        
        print(f"#{T} {global_min}")