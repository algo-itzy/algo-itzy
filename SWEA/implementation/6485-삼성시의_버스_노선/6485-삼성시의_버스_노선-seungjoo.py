
def count_bus(n):
    bus_stops = [0 for _ in range(5000)]
    for _ in range(n):
        start, end = map(int,input().split())
        for i in range(start-1,end):
            bus_stops[i] += 1
    P = int(input())
    qa_set = []
    for i  in range(P):
        qa_set.append(bus_stops[int(input())-1])
    return qa_set
    
for test in range(1, int(input())+1):
    N = int(input())
    answer = count_bus(N)
    print(f'#{test}', end=' ')
    print(*answer)