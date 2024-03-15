n = int(input("Enter the number of elements:"))
arr = list(map(int, input().split()))[:n]
c = 0
for i in range(n-1):
    for j in range(n-i-1):
        if arr[j] > arr[j + 1]:
            c += 1
            arr[j + 1], arr[j] = arr[j], arr[j + 1]
            print(f"sorting step {c}: ", arr)

print()
print("sorted arr: ", arr)
