def calculate_median(list):
    list_size = len(list)

    pivot = int(list_size / 2)

    if list_size % 2 == 0 and list_size != 0:
        return (list[pivot] + (list[pivot] - 1)) / 2
    elif list_size == 0:
        return 'Wrong!'
    else:
        return list[pivot]
try:
    n_ops = int(input('Indique el numero de operaciones:'))

    list = []
    i = 0
    result = []

    while i < n_ops:
        op = input('Indique operacion:').split(' ')

        if op[0] == 'a':
            list.append(int(op[1]))
            list.sort()

        elif op[0] == 'r':

            if len(list) != 0 and int(op[1]) in list:
                list.remove(int(op[1]))

        median = calculate_median(list)
        result.append(median)
        i = i + 1

    print(result)
except:
    print('Algo ha salido mal, verifica el formato de las entradas')
