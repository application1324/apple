#한컴타자을 만들기 위해 무슨 기능이 필요할까?
#1.입력기능
#2.단어, 문장 랜덤 출력
#3.랜덤으로 출력한 단어, 문장에 입력한것이 맞는지 확인
#4.단어, 문장을 램덤 출력을 몇번이상 하면 멈추기

import random

Select= int(input("1.자리연습,2.단어쓰기,3.짧은글 쓰기,4.길글 쓰기 중 무엇을 하시게습니다(숫자입력)."))

if Select == 1:
    print("자리연습을 선택하셌습니다.")
    practice = ["a","b"]
    end = 0
    while end !=2:
        num = random.randrange(1, 2)
        print(practice[num])
        i = input()
        if practice[num] == i:
            end += 1
    print("끝났습니다.")

elif Select == 2:
    print("단어쓰기을 선택하셌습니다.")
    practice1 = ["ab","ba"]
    end1 = 0
    while end1 !=2:
        num1 = random.randrange(1, 2)
        print(practice1[num1])
        i1 = input()
        if practice1[num1] == i1:
            end1 += 1
    print("끝났습니다.")

elif Select == 3:
    print("짧은글 쓰기을 선택하셌습니다.")
    practice2 = ["abc","cba"]
    end2 = 0
    while end2 !=2:
        num2 = random.randrange(1, 2)
        print(practice2[num2])
        i2 = input()
        if practice2[num2] == i2:
            end2 += 1
    print("끝났습니다.")

else:
    print("긴글 쓰기을 선택하셌습니다.")
    practice3 = ["abcd","dcba"]
    end3 = 0
    while end3 !=1:
        num3 = random.randrange(1, 2)
        print(practice3[num3])
        i3 = input()
        if practice3[num3] == i3:
            end3 += 1
    print("끝났습니다.")

