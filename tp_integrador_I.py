def bubble_sort(arr):
    """
    Bubble Sort: recorre la lista varias veces, intercambiando pares adyacentes
    que estén en el orden incorrecto, hasta que no queden más intercambios.
    Complejidad: O(n²) en promedio y peor caso.
    Parámetros:
        arr (list): lista de valores comparables.
    Retorna:
        None (ordena la lista en sitio). Si la lista está vacía, sale sin hacer nada.
    """
# Verificar lista vacía o de un solo elemento: no hay nada que ordenar
    if len(arr) == 0:
        return
    n = len(arr)
# Cada pasada "burbujea" el mayor de los elementos restantes hasta el final
    for i in range(n):
        # En la i-ésima pasada ya están los i mayores al final,
        # por lo que solo recorro hasta n - i - 1
        for j in range(0, n - i - 1):
            # Si el elemento en j es mayor que el siguiente, intercambiamos
            if arr[j] > arr[j + 1]:
                # Intercambio de elementos para que el mayor avance hacia el final
                arr[j], arr[j + 1] = arr[j + 1], arr[j]



if __name__ == "__main__":
    datos = [34, 7, 23, 32, 5, 62]
    print("Lista original:      ", datos)

    # Ordenamiento
    bubble_sort(datos)
    print("Lista ordenada:      ", datos)
