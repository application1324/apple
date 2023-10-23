# 클래스의 이름을 만들때는 대문자로 만든다.
class MyStack:
    stackList = [] # 저장하는 곳
    size = 0

    # construction

    def __init__(self, size):
    # 파이썬에서 생성자을 만들때 사용하는 생성자 규칙
    # 클래스를 사용할 때는 매개변수에는 self가 꼭 들어감, this와 같음
    # self을 사용한 size는 매서드 밖에있는 변수, self가 없으면 안에 있는 매개변수
        self.size = size

    # getter setter

    def push(self, value):
        if len(self.stackList) > self.size:
            return False
        else:
            self.stackList.append(value)
            return True

    def pop(self):
        if len(self.stackList) < 0:
            return False
        else:
            self.stackList.pop()
            return True

    def viwe(self):
        return self.stackList