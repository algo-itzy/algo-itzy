# solved by YoonBaek

def init_dp()->list:
    dp = [0]*int(n + 1)

    return dp

def get_min_ops(n: int):
    #
    for i in range(2, n+1):
        # case -1
        min_ops[i] = min_ops[i-1]+1
        # case / 2
        if not i%2:
            min_ops[i] = min(min_ops[i], min_ops[i//2]+1)
        # case / 3
        if not i%3:
            min_ops[i] = min(min_ops[i], min_ops[i//3]+1)   

    return min_ops[n]


    
if __name__ == "__main__":
    n = int(input())
    min_ops = init_dp()
    
    print(get_min_ops(n))
