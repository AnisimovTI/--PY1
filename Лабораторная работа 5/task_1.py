import pprint


def convert_to_dict():
    representation_list = [{'bin': bin(a), 'dec': a, 'hex': hex(a), 'oct': oct(a)} for a in range(0, 16)]
    return representation_list


pprint.pprint(convert_to_dict())
  #last_string