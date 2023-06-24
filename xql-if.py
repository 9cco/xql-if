import csv

file_path = "output.csv"
default_value = "" # Leave empty string if using code as default.
field_name = "action_file_attributes"
new_field_name = "file_attribute"

# Read the CSV file into a list
try:
    with open(file_path, "r", newline='') as f:
        aux_list = list(csv.reader(f, delimiter=','))
except Exception as e:
    raise e
    
from pprint import pprint

#pprint(aux_list)

xql_stage = f"| alter {new_field_name} = "
xql_end = ''

for line in aux_list[1:]:
    code = int(line[-1].strip())
    meaning = line[0].strip()
    
    xql_stage += f"if({field_name} = {code}, \"{meaning}\", "
    xql_end += ")"

if default_value == "":
    xql_stage += f"to_string({field_name})"
else:
    xql_stage += f"\"{default_value}\""

print( xql_stage, xql_end)
    