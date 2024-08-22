import sys

def ailing_night(N,M):
    if N == 1:
        # 방문한 칸의 개수이고 N=1이면 아예 못움직이니까 
        # 처음 방문한 칸
        answer = 1
        
    elif N == 2:
        # N = 2이면 상하로 1칸씩 밖에 못움직이니까 dy +- 1 밖에 못씀
        # 그리고 M 조건도 있네 그리면 최대 4 구만 그럼 M = 6일때까지 
        # dy +- 1 일때는 dx가 무조건 2 이므로
        # M = 1 -> 1, M=2 -> 1 M=3 -> 2 .... 
        answer = min(M+1//2,4)
            
    else:
        # N>=3이 되어야 2칸씩 움직일 수 있음으로 
        # "4가지 경우를 모두 사용해야한다"라는 명제를 참으로 하기 위한 필요조건
        if M < 7:
            # 근데 M이 6미만이면 dx의 이동을 다 표현 못함. 그래서 4가지 경우 다 안써도 됨
            # 근데 다 dx 1칸 짜리로 이동하면 방문칸이 5가 넘음으로 방문칸의 최대값은 4
            answer = min(M,4)
        else:
            # 6이상이면 무조건 4개다 사용해야한다. 
            # 근데 방문을 최대로 하려면 dx +2가 각각 단 한번만 나오는 것일 때이므로 
            answer = M-2
    return answer


n,m = map(int, sys.stdin.readline().split())
print(ailing_night(n,m))