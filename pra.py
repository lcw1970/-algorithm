def change_num(a) :
    if a == 0 :
        return 1
    else :
        return 0


n = int(input())
switch_lst = list(map(int,input().split()))
students = int(input())
for _ in range(students) :
    zenda,num = map(int,input().split())
    if zenda == 1 :
        
        k = num
        while (k <= n) :
            switch_lst[k-1] = change_num(switch_lst[k-1])
            print(f"스위치 교체: {switch_lst}")
            k += num

    if zenda == 2 :
        p = 1
        if switch_lst[num-1] == 1 :
            switch_lst[num-1] =0 
        else :
            switch_lst[num-1] = 1
        while (num-p >= 0 and num+p < n) :
            if switch_lst[num-p] == switch_lst[num+p] :
                switch_lst[num-p] =change_num(switch_lst[num-p])
                switch_lst[num+p] =change_num(switch_lst[num+p])
                print(f"스위치 교체: {switch_lst}") 
                p += 1
            else :
                break

for i in switch_lst :
    print(i,end = " ")