arr = [7, 5, -8, 10, 1]

N = len(arr) # число элементов в списке

for i in range(0, N-1):
    for j in range(0, N-1-i):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
            
print(arr)
