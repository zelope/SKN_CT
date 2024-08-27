import sys

def file_compile(cnt:int,file_list:list):
    file_list.sort()
    print(file_list)
    dp_graph = [-1]*cnt
    pre_num = -1
    for i,dp in enumerate(file_list):
        if i < 2:
            # 초기값 설정
            if i == 0:
                dp_graph[0] = dp
                pre_num = dp
            else:
                dp_graph[1] = dp + pre_num
                pre_num = dp
        else:
            dp_graph[i]  = min(dp_graph[i-1]*2 + dp, 2*(dp_graph[i-2]+dp+pre_num))
            pre_num = dp
    else:
        answer = dp_graph[cnt-1]
        print(dp_graph)
    return answer



N = int(input())

for _ in range(N):
    M = int(input())
    file_list= list(map(int, sys.stdin.readline().split()))
    print(file_compile(M,file_list))