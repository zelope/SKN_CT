import sys
def solve():
    N = int(input())
    
    #입력받고
    num_arr = [[int(sys.stdin.readline().strip()) for _ in range(N)] for _ in range(N)]
    
    #산술평균
    print(round(sum(num_arr)/len(num_arr)))
    
    #중앙값 -> 정렬 필요 
    num_arr.sort()
    print(num_arr[len(num_arr)//2])
    
    #개수 구하기
    #최빈값
    dic=dict()
    for i in num_arr:#빈도수 구하기
        if i in dic:
            dic[i]+=1
        else:
            dic[i]=1
            
    mx=max(dic.values())#빈도수 중 최대값 구하기
    mx_dic=[]#최빈값 숫자를 저장할 배열

    for i in dic:#빈도수 딕셔너리에서
        if mx==dic[i]:#최빈값의 key저장
            mx_dic.append(i)

    if len(mx_dic)>1:#최빈값이 여러개라면
        print(mx_dic[1])#두번째로 작은 값  3)최빈값
    else:#하나라면
        print(mx_dic[0])#해당 값 출력  3)최빈값
    
    #범위
    print(num_arr[-1] - num_arr[0])
    
    
    
    return None
        
    
    
if __name__ == "__main__":
    
    print(round(4.5))
    print(round(4.55))