def solve():
    for i in range(3,0,-1):
        x = input()
        if x.isdigit():
            number = int(x) + i
    if number % 15 == 0:
        answer = "FizzBuzz"
    elif number % 3 == 0:
        answer = "Fizz"
    elif number % 5 ==0:
        answer = "Buzz"
    else:
        answer = str(number)
    
    print(answer)
    return None
        
    
    
if __name__ == "__main__":
    
    solve()