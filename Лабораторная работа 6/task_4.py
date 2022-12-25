import json

INPUT_FILE = "input.csv"


def csv_to_list_dict(filename) -> list[dict]:
    with open(filename, 'r') as csv:
        headers = csv.readline().strip().split(',')
        to_json = [dict(zip(headers, line.strip().split(','))) for line in csv.readlines()]
        # ПОместил функцию zip в list comprehension, как в замечании
    return to_json


print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))
# end