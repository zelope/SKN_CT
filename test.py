import  sys


def solve():
    n,m = map(int, sys.stdin.readline().split())
    # n = 개수 m = 근점해야하는 값
    n_list = list(map(int, sys.stdin.readline().split()))
    answer = -1 
    
    for i in range(n):
        for j in range(i+1,n):
            for k in range(j+1,n):
                b_force = n_list[i]+n_list[j]+n_list[k]
                
                if (b_force <= m) and (b_force > answer):
                    answer = b_force
    
    return answer

if __name__ == "__main__":
    
    print(solve())