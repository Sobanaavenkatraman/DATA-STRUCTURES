n = int(input("Enter the number of elements:"))
arr = list(map(int, input(f"Enter only {n} elements: ").split()))
# 23 8 34 98 2 12 33
for i in range(1, n):
    j = i
    while j > 0 and arr[j] < arr[j - 1]:
        arr[j], arr[j - 1] = arr[j - 1], arr[j]
        j -= 1
print("Sorted arr: ", arr)


