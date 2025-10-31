def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def partial_sort(arr, left, right, k):
    if left < right and k > 0:
        pi = partition(arr, left, right)
        
        if pi == k - 1:
            return
        elif pi > k - 1:
            partial_sort(arr, left, pi - 1, k)
        else:
            partial_sort(arr, pi + 1, right, k)

def main():
    print("Partial Sort Program")
    print("-" * 40)
    
    arr_input = input("Enter numbers separated by spaces: ")
    arr = list(map(int, arr_input.split()))
    
    k = int(input("Enter k (number of smallest elements to sort): "))
    
    if k > len(arr):
        k = len(arr)
    
    print(f"\nOriginal array: {arr}")
    
    partial_sort(arr, 0, len(arr) - 1, k)
    
    print(f"After partial sort (first {k} elements sorted): {arr}")
    print(f"Smallest {k} elements: {arr[:k]}")

if __name__ == "__main__":
    main()