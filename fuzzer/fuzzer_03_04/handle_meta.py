def handle_meta(meta):
    for key, value in meta.items():
        if key == 'file-extension':
            file_extension = value
        elif key == 'endian':
            endianness = value
        elif key == 'id':
            id = value
            
    return endianness, file_extension,id