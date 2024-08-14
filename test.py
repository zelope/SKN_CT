import re
def _cnt_updown(name_chr:str) -> int:
    answer = ord(name_chr) - ord("A")
    if answer > 12:
        answer = 26 - answer
    
    return answer

def _cnt_rightleft(name:str) -> int:
    pattern = r"A+"
    matches = re.findall(pattern,name)
    if matches:
        cnt_A = max(len(match) for match in matches)
    else:
        cnt_A = 0
    answer = len(name) - (cnt_A+1)
    if answer < 0:
        answer = 0
    return answer


def solution(name):
    answer = _cnt_rightleft(name)
    for n_chr in name:
        answer += _cnt_updown(n_chr)
    return answer

if __name__ == "__main__":
    input_name = "JEROEN"
    print(solution(input_name))
    