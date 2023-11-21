# bubble sort
# 제일 큰 숫자을 뒤로 보내는 것
num = [6,4,3,2,1,8,9,5,7]

# 큼 > 작음

cnt = 0
swap = 0
for i in range(len(num)):
    for j in range( len(num)- (i+1)):
        cnt += 1
        if num[j] > num[j+1]:
            swap += 1
            t = num[j]
            num[j] = num[j+1]
            num[j+1] = t
            print(f'{num[j]}{num[j+1]}')
print(num)
print(cnt)
print(swap)