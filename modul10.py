def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

def binary_search(arr, target):
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1

def main():
    input_list = [87, 56, 34, 23, 89, 15, 2, 200, 28, 3]
    angka_input = int(input("Masukkan angka yang dicari: "))

    bubble_sort(input_list)

    print("Setelah di sorting:", input_list)

    index = binary_search(input_list, angka_input)

    if index != -1:
        print(f"Angka {angka_input} terdapat di elemen ke-{index}")
    else:
        print(f"Angka {angka_input} tidak ditemukan dalam list")

if __name__ == "__main__":
    main()
