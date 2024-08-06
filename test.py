import sys
from collections import deque

CNT = int(sys.stdin.readline().strip())

for _ in range(CNT):
    value_dict = dict()
    index_deque = deque([])
    importance_list = list()
    
    N,M = map(int,sys.stdin.readline().split())
    input_list = map(int,sys.stdin.readline().split())
    
    
    order = 0
    
    for i,ele in enumerate(input_list):
        str_i = str(i)
        value_dict[str_i] = ele
        index_deque.append(str_i)
        importance_list.append(ele)
    
    importance_list.sort(reverse=True)
    
    importance_deque = deque(importance_list)
    while len(index_deque) > 0:
        is_target = index_deque[0]
        if  value_dict[is_target] == importance_deque[0]:
            importance_deque.popleft()
            index_deque.popleft()
            order += 1
            if is_target == str(M):
                print(order)
                break
        else:
            index_deque.rotate(-1)
            
    
    