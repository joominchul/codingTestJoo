#https://school.programmers.co.kr/learn/courses/30/lessons/42892?language=python3#
import sys 
sys.setrecursionlimit(10000) #재귀 한도 증가

class BSTNode: #노드 정보 저장 클래스
    def __init__(self, key, value):
        self.key = key      #노드의 x값
        self.value = value  #노드 번호
        self.left=None
        self.right = None

def insert_bst(r, n):                       #너비 우선 탐색
        if n.key<r.key:                     #루트의 x값보다 작은 경우
            if r.left is None:              #왼쪽 자식이 없으면 왼쪽 자식 노드로 설정
                r.left = n
                return True
            else:
                return insert_bst(r.left, n)#왼쪽 자식이 있으면 재귀
        elif n.key>r.key:                   #루트의 x값보다 큰 경우
            if r.right is None:             #오른쪽 자식이 없으면 오른쪽 자식 노드로 설정
                r.right = n
                return True
            else:
                return insert_bst(r.right, n)#오른쪽 자식이 있으면 재귀
        else:
            return False

def preorder(n, l) :		#전위 순회(노드, 리스트)
    if n is not None :
        l.append(n.value)   #l 리스트에 노드의 value 추가
        preorder(n.left,l)	#노드의 왼쪽 자식 호출
        preorder(n.right,l)	#노드의 오른쪽 자식 호출

def postorder(n, l) :       #후위 순회(노드, 리스트)
    if n is not None :
        postorder(n.left,l) #노드의 왼쪽 자식 호출
        postorder(n.right,l)#노드의 오른쪽 자식 호출
        l.append(n.value)   #l 리스트에 노드의 value 추가
        
class BSTMap(): #이진트리 저장 맵
    def __init__(self):
        self.root = None
    def isEmpty(self): #트리가 비어있는지 확인
        return self.root == None
    
    def insert(self, key, value):   #삽입 함수
        n = BSTNode(key, value)     #노드 정보를 BSTNode로 설정
        if self.isEmpty():          #트리가 없으면 n을 루트 노드로 설정
            self.root = n
        else:                       #트리가 있으면
            insert_bst(self.root, n)#insert_bst 호출
    def make(self):                 #정답을 리턴하는 함수
        answer = []                 #정답 저장 리스트
        pre = []                    #전위 순회 값 저장 리스트
        post = []                   #후위 순회 값 저장 리스트
        preorder(self.root, pre)    #전위 순회 함수 호출
        postorder(self.root, post)  #후위 순회 함수 호출
        answer.append(pre)
        answer.append(post)
        return answer               #전위 순회 리스트와 후위 순회 리스트를 추가한 후 리턴

map = BSTMap()
def solution(nodeinfo):
    answer = [[]]
    level = {}  #y값에 따라 노드들을 저장할 딕셔너리
    root = 0    #가장 큰 y값(루트 노드의 y값)을 저장할 변수
    for i in range(len(nodeinfo)):                                  #노드들의 정보를 level 딕셔너리에 저장
        if root<nodeinfo[i][1]:                                     #루트 설정
            root = nodeinfo[i][1]
        temp = level.get(nodeinfo[i][1])
        if temp:                                                    #딕셔너리에 y값 키가 있으면
            temp.append([nodeinfo[i][0], i+1])                      #값에 노드 정보 추가
            level[nodeinfo[i][1]] = temp
        else:                                                       #키가 없으면
            level.update({nodeinfo[i][1]: [[nodeinfo[i][0], i+1]]}) #{y값 키: [[x값, 노드 번호]]} 업데이트
    for i in range(root, -1, -1):       #y값이 큰 순서대로(루트부터 아래로) 이진트리에 추가
        temp = level.get(i)
        if temp:                        #i와 같은 y값 키가 있으면
            for n in temp:
                map.insert(n[0], n[1])  #이진트리에 (x값, 노드 번호) 추가
    answer = map.make() #정답 리턴
    return answer
