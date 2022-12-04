def delete(list_, index=None):

    if index is None:  # значение по умолчанию - None
        index = -1
        list_slice = list_[:index]  # срезаем последний
    else:
        list_slice = list_[:index] + list_[(index + 1):]  # срезаем следующий

    return list_slice

print(delete([0, 1, 2], index=0))  # [0, 1]
print(delete([0, 1, 2], index=1))  # [0, 2]
print(delete([0, 1, 2]))  # [0, 1]
