def bubble_sort_recursive(arr, n):
    if n == 1:
        return

    for i in range(n - 1):
        if arr[i] > arr[i + 1]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]

    bubble_sort_recursive(arr, n - 1)

def main():
    input_list = [87, 56, 34, 23, 89, 15, 2, 200, 28, 31]

    print("List yang belum di-sorting:")
    print(input_list)

    bubble_sort_recursive(input_list, len(input_list))

    print("List yang sudah di-sorting:")
    print(input_list)

if __name__ == "__main__":
    main()
