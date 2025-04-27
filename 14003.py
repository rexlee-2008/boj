import sys
from bisect import bisect_left

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

# LIS 계산
lis = []
temp = [-1] * n  # LIS에서 각 위치의 인덱스를 저장
prev = [-1] * n  # LIS를 복원하기 위한 이전 인덱스 저장

for i in range(n):
    pos = bisect_left(lis, arr[i])  # LIS에서 arr[i]가 들어갈 위치 찾기
    if pos < len(lis):
        lis[pos] = arr[i]
    else:
        lis.append(arr[i])
    
    temp[pos] = i  # LIS에서 현재 위치의 인덱스 저장
    if pos > 0:
        prev[i] = temp[pos - 1]  # 이전 인덱스 저장

# LIS 복원 (중복 포함)
result = []
index = temp[len(lis) - 1]
while index != -1:
    result.append(arr[index])
    index = prev[index]

# 결과 출력
print(len(lis))
print(' '.join(map(str, result[::-1])))

'''
result = []
index = lis_indices[length - 1]
while index != -1:
    result.append(arr[index])
    index = prev_indices[index]

print(' '.join(map(str, result[::-1])))
'''

'''
6
10 20 10 30 20 50
'''