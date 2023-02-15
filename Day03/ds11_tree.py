#이진 탐색트리 구현

class TreeNode():
    def __init__(self) -> None:
        self.left = None
        self.data = None
        self.right = None

# 전역변수 선언
memory = []
root = None
nameAry = ['블랙핑크', '레드벨벳', '마마무', '걸스데이', '트와이스','에이핑크']

# if __name__ == '__main__':
node = TreeNode()
node.data = nameAry[0] #블랙핑크
root = node
memory.append(node) #memory에 node를 집어 넣는다

for name in nameAry[1:]:

    node = TreeNode()
    node.data = name

    current = root
    while True:
        if name < current.data: # 부모노드 왼쪽으로
            if current.left == None:
                current.left = node
                break
            current = current.left
        else: # 부모노드 오른쪽
            if current.right == None:
                current.right = node
                break
            current = current.right
    memory.append(node)


print('이진 탐색트리 구성완료')

print(root.data)
print(f'{root.left.data, root.left.left.data, root.left.right.data}왼쪽 이진트리')
print(f'{root.right.data, root.right.left.data}오른쪽 이진트리')

search = input('찾을 걸그룹을 입력 >')
current = root
while True:
    if search == current.data:
        print(search, '찾음, 끝')
        break
    elif search < current.data: # 왼쪽으로
        if current.left == None:
            print(search, '못찾음 끝!')
            break
        current = current.left
    else: # 오른쪽 노드로
        if current.right == None:
            print(search, '못찾음, 끝')
            break
        current = current.right