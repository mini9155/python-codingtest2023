# 스택 활용

# 줄 잘 맞추기
import ds04_stack as st

import webbrowser # 웹사이트를 띄우기 위해 쓰는 모듈
import time

st.SIZE = 100
st.stack = [None for _ in range(st.SIZE)]
st.top = -1

if __name__ == '__main__':
    urls =['www.naver.com','www.daum.net','www.nate.com','www.google.com']

    for url in urls:
        st.push(url)
        webbrowser.open(f'https://{url}')
        print(url, end='-->')
        time.sleep(1) # 1초동안  일시정지

    print('방문 종료')
    time.sleep(1)

    while True:
        url = st.pop()
        if url == None:
            break
            
        else:
            webbrowser.open(f'https://{url}')
            print(url, end='-->')
            time.sleep(1)
    print('재방문 종료')
    print(st.stack)

    input('꺼지지말고 기다려!!')
