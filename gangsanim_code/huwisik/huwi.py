2+3*4/5
#변환 시작!

#1. 괄호로
# (2+((3*4)/5))
# ((2+(34*/5))
# (2+34*5/)
# 34*5/2+
# 괄호 뒤에 해당 토큰 기재

# 2. 스택으로 변환
# 연산자가 나타나면 우선순위 낮은 피연산자까지 pop()
def huwi(sik):
    # push 전에 조건비교로 해결 값에 연연x
    if sik == '*' or '/':
        while top == '*' or top == '/':
            pop()
        push(sik)
    elif sik == '+' or '-':
        while top != '(':
            pop()
    elif sik == ')':
        while top == '(':
            pop()
    else:
        push()

for x in sik:
    if x가 숫자:
        print(x)
    else:
        huwi(x)



a = '2+3*4/5'

b = '2+3*4+5'


