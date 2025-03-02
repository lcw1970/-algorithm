# my code
n = int(input())
n_lst = list(map(int,input().split()))
n_dic = {}

nsort_lst= sorted(set(n_lst)) 

for i in range(len(nsort_lst)) :
    n_dic[nsort_lst[i]] = i 

for i in n_lst :
    print(n_dic[i],end = " ")

# n = int(input())          gpt code
# n_lst = list(map(int, input().split()))

# # 중복 제거 후 정렬
# nsort_lst = sorted(set(n_lst))

# # 숫자 → 압축된 값 변환 딕셔너리 생성
# n_dic = {num: idx for idx, num in enumerate(nsort_lst)}

# # 원래 리스트를 압축된 값으로 변환하여 출력
# print(*[n_dic[num] for num in n_lst])  # 리스트를 언패킹해서 공백 구분 출력
