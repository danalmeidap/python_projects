def swap_bubble(x, y):
    if x > y:
        aux = x
        x = y
        y = aux
    return x, y


def bubble_sort(array):
    """
    Função para realizar um bublle sort e organizar determinado array. Nesse método em questãom faço uma abordagem com
    loop while
    :param array: lista de números a serem organizados
    :return: Retorna o array já organizado
    """
    elements = len(array) - 1
    is_sorted = False
    while not is_sorted:
        is_sorted = True
        for i in range(elements):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                is_sorted = False
    return array


def bubble_2(array):
    numbers = array[:]

    def sort(arr, n):
        if n == 1:
            return arr
        else:
            for i in range(0, n):
                for j in range(i + 1, n):
                    arr[i], arr[j] = swap_bubble(arr[i], arr[j])
            return sort(arr, n - 1)
    return sort(numbers, len(numbers) - 1)


numbers_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
print(bubble_sort(numbers_list))
print(bubble_2(numbers_list))
