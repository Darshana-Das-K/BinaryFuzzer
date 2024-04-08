import os
import yaml


from handle import handle_seq
from handle_meta import handle_meta

output_directory = 'testcases'
os.makedirs(output_directory, exist_ok=True)
# Specify the path to your YAML file
file_path = '/Users/darshanadask/mini_project/Working_area/fuzzer0304/example.ksy'

# Read the YAML data from the file
with open(file_path, 'r') as file:
    yaml_data = file.read()

# Load YAML data
data_tree = yaml.safe_load(yaml_data)
print(data_tree)

# Call the functions with explicit parent information


# Write to file

for i in range(0, 100):
    endianness, file_extension = handle_meta(data_tree['meta'])
    expansion = handle_seq(data_tree['seq'], endianness, data_tree)
    
    # Determine the file path
    filename = f"output{i}.{file_extension}" if file_extension else f"output{i}"
    filepath = os.path.join(output_directory, filename)
    
    # Write the output to the file
    with open(filepath, 'wb') as file:
        file.write(expansion)