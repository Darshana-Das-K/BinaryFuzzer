import struct
def pack_value(value, endianness):
    if isinstance(value, int):
        binary_data = struct.pack(f'{endianness}B', value)  # Use 'H' for unsigned short integer
    elif isinstance(value, float):
        binary_data = struct.pack(f'{endianness}d', value)  
    elif isinstance(value, str):
        string_bytes = value.encode('utf-8')
        binary_data = struct.pack(f'{endianness}{len(string_bytes)}s', string_bytes)

    return binary_data