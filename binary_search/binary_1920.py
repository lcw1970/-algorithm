import sys
input = sys.stdin.read
input_data = input().split()

n = int(input_data[0])
n_lst = list(map(int, input_data[1:n + 1]))
m = int(input_data[n + 1])
m_lst = list(map(int, input_data[n + 2:]))

n_lst.sort()

def binary(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return 1
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return 0

for i in m_lst:
    print(binary(n_lst, i, 0, n - 1))