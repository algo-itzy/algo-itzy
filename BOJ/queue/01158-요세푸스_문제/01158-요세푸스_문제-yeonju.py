N, K = map(int, input().split()) # N 는 총 인원, K 는 제거될 K 번째 사람
q = [] 
result = [] # 요세푸스 순열에 담을 순서 리스트

for i in range(N): 
    q.append(i+1) # 1~ N 까지의 수를 큐에 담아놓음
    c = 0 
    
while len(q) > 0: # 큐가 비게 될 때까지
    c = (c + (K-1)) % len(q) #12 4567 에서 
    cc = q.pop(c)  # pop 은 지정한 위치 값을 제거하는 것
    result.append(str(cc)) # 제거된 사람을 result 리스트에 담음

print("<%s>" %(", ".join(result)))