import random
import timeit
from tp_integrador_I import bubble_sort

def crear_lista(n):
    return random.sample(range(1, n * 10), n)

if __name__ == "__main__":
    for tamaño in [10, 50, 100, 500, 1000]:
        lista = crear_lista(tamaño)
        # Medir tiempo de Bubble Sort
        tiempo_bubble = timeit.timeit(lambda: bubble_sort(lista.copy()), number=10)
        # Medir tiempo de sorted() nativo
        tiempo_sorted = timeit.timeit(lambda: sorted(lista), number=10)
        print(f"Tamaño {tamaño}: Bubble Sort = {tiempo_bubble:.4f} s; sorted() = {tiempo_sorted:.4f} s")
