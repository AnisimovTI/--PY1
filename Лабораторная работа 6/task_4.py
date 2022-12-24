import json

INPUT_FILE = "input.csv"


def csv_to_list_dict(filename) -> list[dict]:
    with open(filename, 'r') as input:
        input_data = input.readlines()
        input_data = [string.strip() for string in input_data] # удаляем символ новой строки в конце каждой строки в списке
        input_data = [string.split(',') for string in input_data] # создаем список списков на основе input_data
        # разобиваем список на заголовки и данные 
        headers = input_data[0]
        rows = input_data[1:]
        # создаем возвращаемый список словарей
        list_of_dict_for_json = []
        # заполняем список, проходя по подспискам в списке данных
        for row in rows:
            dict_for_json = {}
            for i, value in enumerate(row):
                dict_for_json[headers[i]] = value
            list_of_dict_for_json.append(dict_for_json) # добавляем заполненный для row словарь в список-результат
    return list_of_dict_for_json
        
    
print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))
