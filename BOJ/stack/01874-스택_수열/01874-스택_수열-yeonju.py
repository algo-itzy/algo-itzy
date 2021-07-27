 import sys
 
 N = int(input()) # N 까지의 수를 입력 받음
 
 st = [] 
 result = []
 cnt = 1
 temp = True
 
 for i in range (N) :
     num = int(input()) # 입력시킬 수열의 원소들이 하나씩 주어짐
    
     while cnt <= num : # 입력 받은 수가 cnt 보다 작거나 같은 경우, 스택에 push 
         st.append(cnt)
         result.append('+')
         cnt += 1 
        if st[-1] == num : #스택의 마지막에 있는 원소가 num 랑 같을 경우, 스택에서 pop
            st.pop()
            result.append('-')
        else :
            temp = False

if temp == False : #입력된 수열을 못 만드는 경우 
    print('NO')
else : 
    for i in result :
        print(i)