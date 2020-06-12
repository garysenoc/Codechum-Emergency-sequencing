arr = [0,1,4]

num = int(input())

add = 3;
add2 = 4;
last = arr[2]
if(num>2):
    for i in range(3,num):
        arr.append(add + add2+last)
        add = ((i-1) * 2) + add
        add2 = add2+2
        last = arr[i]
for i in range(0,num):
    print(arr[i],end=" ")
