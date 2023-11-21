# 0,1,2,3,4 * 3
cnt = 0
for i in range(3):
    # 3번
    print(f'i = {i}')
    for j in range(5):
        # 0,1,2,3,4
        cnt += 1
        print(j)
print(cnt)