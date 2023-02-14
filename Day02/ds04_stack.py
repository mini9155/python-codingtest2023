#스택 전체 구현
#스택이 꽉 찾는 지  확인
# global전역 변수
SIZE = 0
stack = []
top = -1


#함수 선언 부분
def isStackFull():
    global SIZE, stack, top # 전역변수를 그대로 함수에서도 쓸꺼야

    if (top >= SIZE-1): #  만약 top이 SIZE-1보다 크면
        return True
    else:
        return False
#스택이 비어있는지 여부 확인
def isStackEmpty():
    global SIZE, stack, top # 전역변수를 그대로 함수에서도 쓸꺼야

    if (top == -1): #  만약 top이 -1이면
        return True
    else:
        return False

# 스택에 데이터 추가

def push(data):
    global SIZE, stack, top
    if (isStackFull()):
        print('Stack is Full')
        return
    else:
        top += 1
        stack[top] = data

# 스택에서 데이터 추출

def pop():
    global SIZE,stack, top
    if (isStackEmpty()):
        print('Stack is Empty!')
        return None
    else:
        data = stack[top]
        stack[top] = None
        top -= 1
        return data

# top의 데이터 확인
def peek():
    global SIZE, stack, top
    if isStackEmpty():
        print('Stack is Empty')
        return None
    else:
        return stack[top]

#열심히 합시다!

#메인 엔트리


# if __name__ == '__main__':
#     top = -1
#     SIZE = int(input('스택 사이즈 입력 >>'))
#     stack = [None for _ in range(SIZE)]

#     while True:
#         select = input('삽입(I)/추출(E)/확인(V)/종료(X) >> ')

#         if select.lower() == 'x': # 종료
#             break
#         elif select.lower() == 'i':
#             data = input('추가할 데이터 >> ')
#             push(data)
#             print(f'스택상태:{stack}')
#         elif select.lower() == 'e': #추출
#             data = pop()
#             print(f'추출데이터 : {data}')
#             print(f'스택상태 : {stack}')
#         elif select.lower() == 'v': #확인
#             data = peek()
#             print(f'확인 데이터 : {data}')
#             print(f'스택상태 : {stack}')
#         else:
#             continue
#     print('프로그램 종료')
