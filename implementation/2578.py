def found(num) :
    for k in range(5):
        for t in range(5):
            if lst[k][t] == num :
                lst[k][t] = 0 

def count_bingo() :
    bingo_count = 0
    for n in range(5):
        for m in lst[n] :
            if m != 0 : 
                break
        else :
            bingo_count += 1
    for j in range(5):
        for i in range(5):
            if lst[i][j] != 0:
                break
        else :
            bingo_count += 1
    
    

    if lst[0][0]==0 and lst[1][1]==0 and lst[2][2]==0 and lst[3][3]==0 and lst[4][4]==0:
        bingo_count += 1


    if lst[0][4]==0 and lst[1][3]==0 and lst[2][2]==0 and lst[3][1]==0 and lst[4][0]==0:
        bingo_count += 1
    return bingo_count

lst = []
bingo = []

for _ in range(5) :
    lst.append(list(map(int,input().split())))

for _ in range(5) :
    bingo.append(list(map(int,input().split())))
count = 0
for i in range(5):
    for j in range(5):
        num = bingo[i][j]
        count += 1
        found(num)
        bingo_count = count_bingo()

        if bingo_count >= 3 :
            print(count)
            exit()