import re


def solve(expression:str):
    m_ans = eval(expression)
    #문자열을 수식 계산
    
    token = re.findall(r'\d+|\+|\-|\*|\/',expression)
    # \d+ or + or - or * or / 과 매칭되는 것들을 찾아서 리스트로 반환
    # \d+ 는 한개 이상의 숫자로 이루어진 것
    print(token)
    
    f_ans = int(token[0])
    for tag in range(1,len(token),2):
        if token[tag] == "+":
            f_ans += int(token[tag+1])
        elif token[tag] == "-":
            f_ans -= int(token[tag+1])
        elif token[tag] == "*":
            f_ans *= int(token[tag+1])
        elif token[tag] == "/":
            f_ans /= int(token[tag+1])
        else:
            pass
    
    return m_ans, f_ans

if __name__ == "__main__":
    
    male, female = solve("123+45*2-8/4")
    
    print(f'철수 : {male}')
    print(f'영희 : {female}')