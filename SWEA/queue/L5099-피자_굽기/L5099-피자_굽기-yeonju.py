# 구글링해서 참고해서 풀었습니다.....

t = int(input())

for tc in range(t):
    n, m = map(int, input().split())                  # 화덕의 크기 n, 피자의 개수 m

    cheese = input().split()                          # 피자에 치즈가 뿌려진 양 ci
    pizza = [(i+1, int(cheese[i])) for i in range(m)] # 피자 번호와 그 피자에 뿌려진 치즈의 양을 묶어서 리스트에 저장 

    pizzas = pizza[:n]                                # 화덕의 크기만큼 피자 집어넣기 

    pizza = pizza[n:]                                 # 화덕에 못 들어갔던 피자   

    while len(pizzas) != 1:  
        num, cheese = pizzas.pop(0) 
        cheese//=2                                   

        if cheese:                                 # 치즈가 있다면, 다시 화덕에 넣기
            pizzas.append((num, cheese))
        else: 
            if pizza: 
                pizzas.append(pizza.pop(0))

    print(f'#{tc+1} {pizzas.pop()[0]}') 

