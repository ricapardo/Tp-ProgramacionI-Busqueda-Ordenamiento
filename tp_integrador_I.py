def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]



if __name__ == "__main__":
    datos = [34, 7, 23, 32, 5, 62]
    print("Lista original:      ", datos)

    # Ordenamiento
    bubble_sort(datos)
    print("Lista ordenada:      ", datos)
