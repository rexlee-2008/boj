n = int(input())
l = list(map(int, input().split()))
count = 0
def bubble_sort(arr):
    global count
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                count += 1
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
bubble_sort(l)
print(l,count)
'''
3
3 2 1
'''