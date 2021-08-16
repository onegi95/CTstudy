## 내 실력으로 어려움
a = input()

length = len(a)//2
result = []
    
for i in range(length):
    sub_list = []
    for j in range(0, len(a), i+1):
        sub_list.append(a[j:j+i+1])
    result.append(sub_list)

r_result = []
for i in result:
    s_list = ''
    cnt = 1
    for j in range(0, len(i)-1):
        if i[j] == i[j+1]:
            cnt += 1
        else:
            if cnt == 1:
                s_list += i[j]
            else:
                s_list += str(cnt)
                s_list += i[j]
            cnt = 1
    if cnt == 1:
        s_list += i[j]
    else:
        s_list += str(cnt)
        s_list += i[j]
    
    r_result.append(s_list)
print(r_result)

len_list = []
for i in r_result:
    len_list.append(len(i))

print(min(len_list))
    
        


