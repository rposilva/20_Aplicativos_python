import time

def bubble_sort_visual(lista):
    n = len(lista)

    for i in range(n - 1):
        for j in range(n - 1 - i):
            print(f"Comparando {lista[j]} e {lista[j+1]}... ", end="")
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                print("Trocou!")
            else:
                print("Não trocou.")
            print("Estado atual:", lista)
            time.sleep(0.5)  # Pausa para simular animação
        print(f"Fim da rodada {i+1}: {lista}\n")
    return lista

# Teste
valores = [5, 1, 4, 2, 8]
print("Antes:", valores)
ordenado = bubble_sort_visual(valores)
print("Depois:", ordenado)
# Teste com lista vazia
