"""
tp_integrador_I.py

Contiene dos funciones principales:
- bubble_sort(arr)
- binary_search(arr, target)

Al ejecutar este script directamente, ordena una lista de ejemplo
y busca un elemento para mostrar cómo funciona cada algoritmo
"""
def binary_search(arr, target):
    """
    Búsqueda Binaria: en una lista ordenada, divide iterativamente el rango de búsqueda.
    Complejidad: O(log n).
    Parámetros:
        arr (list): lista ordenada de valores comparables.
        target: valor a buscar dentro de 'arr'.
    Retorna:
        (int) índice en el que se encontró 'target', o -1 si no se encuentra.
    """
    # Si la lista está vacía, no tiene mucho sentido hacer más operaciones
    if len(arr) == 0:
        return -1

    low, high = 0, len(arr) - 1

    # Mientras el rango [low..high] siga siendo válido
    while low <= high:
        mid = (low + high) // 2
        # Caso de éxito: arr[mid] coincide con target
        if arr[mid] == target:
            return mid
        # Si el valor en mid es menor, descartamos la mitad izquierda
        elif arr[mid] < target:
            # El nuevo límite inferior se mueve justo después de mid
            low = mid + 1
            # Comentario: descartamos todo índice <= mid porque arr[mid] < target
        else:
            # Caso arr[mid] > target: descartamos la mitad derecha
            high = mid - 1
            # Comentario: descartamos todo índice >= mid porque arr[mid] > target

    # Si salimos del while, significa que low > high y no encontramos target
    return -1


if __name__ == "__main__":
    # Lista de ejemplo desordenada
    datos = [34, 7, 23, 32, 5, 62]
    print("Lista original:      ", datos)

    # Buscamos un valor dentro de la lista ordenada
    objetivo = 23
    pos = binary_search(datos, objetivo)
    if pos != -1:
        print(f"Elemento {objetivo} encontrado en posición {pos}.")
    else:
        print(f"Elemento {objetivo} NO encontrado.")
