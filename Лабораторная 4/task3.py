def delete(list_, index=None):
    if index is None:
        return list_[:-1] # для пустого значения
    else:
        if index == -1:
            return list_[:index] # для index = -1
        else:
            return list_[:index] + list_[index + 1:] # для положительных и отрицательных значений

print(delete([0, 1, 2], index=0))  # [0, 1]
print(delete([0, 1, 2], index=1))  # [0, 2]
print(delete([0, 1, 2]))  # [0, 1]
print(delete([0, 1, 2], index=-1)) # проверка отрицательных значений
print(delete([0, 1, 2], index=-2)) # проверка отрицательных значений
print(delete([0, 1, 2], index=-3)) # проверка отрицательных значений
 # Ответ