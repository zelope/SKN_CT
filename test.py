import  sys


def solve():
    n = int(input())
    size_list = list(map(int, sys.stdin.readline().split()))
    t, p = map(int, sys.stdin.readline().split())
    p_ans = n // p
    p_rest = n % p
    t_ans = 0
    for size in size_list:
        if size == 0:
            continue
        need = size // t
        if size%t == 0:
            t_ans += need
        else:
            t_ans += need+1
    print(f'We need {t_ans} T-shirt bundle \n We need {p_ans} pencil bundle and {p_rest} pieces')
    return None

if __name__ == "__main__":
    
    solve()