from random_generate import random_based_on_type, random_based_on_size
from pack_list import pack_list
#from handle_type import handle_type

def handle_seq(seq, endian, parent):
    expansion = b''

    for item in seq:
        type = None
        size = 0
        encoding = None
        endianness= '<' if endian == 'le' else '>'
        valid_endian= 'big' if endian=='le' else 'little'
        for key, value in item.items():
            if key == 'contents':
                expansion += pack_list(value,endianness)
            elif key == 'size':
                size = value
            elif key == 'type':
                type = value
            elif key == 'encoding':
                encoding = value
            elif key=='valid':
                expansion+= value.to_bytes((value.bit_length() + 7) // 8, valid_endian)

        if type is None:
            expansion += random_based_on_size(size, endianness)
        elif type in ['u2', 'u4', 'u8', 's2', 's4', 's8', 'str', 'f2', 'f4', 'f8']:
            expansion += random_based_on_type(size, type, endianness, encoding)
        else:
            expansion += handle_type(parent['types'],endian,type)
    return expansion
def handle_type(types,endianness,user_defined_type):
    expansion = b''
    for key, value in types.items():
        if key== user_defined_type:
            expansion += handle_seq(types[key]['seq'], endianness, types[key])
    return expansion

