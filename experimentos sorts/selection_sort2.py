def selection_sort(array, invert=False):
    """
    Função para Realizar um selection sort e, organizar determinado array
    :param array: Conjunto de números a serem organizados
    :param invert: Valor booleano que vai determinador se eu quero a lista organizada em ordem direta ou não.
    :return: Retorna a lista organizada, sejam em ordem crescente ou decrescente. De acordo com o parâmetro invert
    """
    numbers = array
    for i in range(0, len(numbers)):
        min_index = i
        for j in range(i + 1, len(numbers)):
            if invert:
                if numbers[min_index] < numbers[j]:
                    min_index = j
            else:
                if numbers[min_index] > numbers[j]:
                    min_index = j
        numbers[i], numbers[min_index] = swap(numbers[i], numbers[min_index])
    return numbers


def swap(x, y):
    aux = x
    x = y
    y = aux
    return x, y


numbers_list = []
array_size = int(input("Array size:"))
for c in range(0, array_size):
    number = int(input(f'{c + 1}º number:'))
    numbers_list.append(number)

print(numbers_list)
print(selection_sort(numbers_list))
