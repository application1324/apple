import my_stack as st
# stack1 = st.MyStack(size=5)
# stack2 = st.MyStack(size=10)

stack = [st.MyStack(size=5), st.MyStack(size=10)]

while True:
    action = input('동작을 입력하세요, 1번조작, 2번조작, q나가기')
    if action == 'q':
        break
    else:
        target = int(action)-1
        act = input('1.push, 2.pop, 3.view')
        if act == '1':
            val = ('값을 입력하세요')
            if stack[target].push(value= val) == True:
               print('성공')
            else:
                print('실패')
        elif act == '2':
            print()
        elif act == '3':
            print()