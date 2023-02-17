# C:\Windows\System32 출력
import os

#print(dir(os)) # os가 담고 있는 함수

# fnameary = []
# folder = 'C:\Windows\System32'
# for dirname, surdirlist, fnames in os.walk(folder):
#     for fname in fnames:
#         fnameary.append(fname)

# print(len(fnameary))]


def makefilelist(folder):
    fnameary = []
    for _,_, fnames in os.walk(folder):
        for fname in fnames:
            fnameary.append(fname)
    
    return fnameary

def insertionsort(ary):
    n = len(ary)
    for end in range(1, n): # 앞의 값 하나 뺴고 끝까지 반복
        for cur in range(end, 0, -1):
            if ary[cur -1] > ary[cur]:
                tmp = ary[cur -1]
                ary[cur -1] = ary[cur]
                ary[cur] = tmp
    return ary

fileary = makefilelist('C:\Program Files\Common Files')
fileary = insertionsort(fileary)
print('파일명 역순 -->', fileary)