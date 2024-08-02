def solve():
    N = int(input())
    
    #입력받고
    score_list = [int(input()) for _ in range(N)]
    #정렬하고
    score_list.sort()
    #위 아래 0.15씩 삭제하고
    trim = round(N*0.15)
    trimed_list = score_list[trim:-1*trim]
    
    #평균 구하고
    avg = sum(trimed_list)/len(trimed_list)
    
    #평균도 반올림하고
    answer = round(avg)
    print(answer)
    
    return None
        
    
    
if __name__ == "__main__":
    
    solve()