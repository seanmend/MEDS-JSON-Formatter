import sys
import json


# input ex: JSON object with entries in this format "1734": "Non Medicaid Florida Community Care",
# output ex: Complete list in this format
# [
#   {
#     "code": "1734",
#     "item": "Non Medicaid Florida Community Care"
#   }
# ]

# *** Make Sure To Update 'Add New Entry' BEFORE running ***

def meds_json_formatter(json_path):
    output_list = []
    if not json_path:
        raise RuntimeError

    # Opening JSON file
    f = open(json_path)

    # returns JSON object as a dictionary
    data = json.load(f)

    keys = data.keys()
    length_of_list = len(keys)

    # Format existing
    for i in range(1, length_of_list + 1):
        key = list(data)[i - 1]
        value = list(data.values())[i - 1]
        output_list.append({"code": key, "item": value})

    # Add New Entry
    new_key = '1734'  # ********************  EDIT THIS  ************************
    new_val = 'Florida Community Care'  # ********************  EDIT THIS  ************************
    output_list.append({"code": new_key, "item": new_val})

    # Saving Result locally as output.txt
    result = json.dumps(output_list)
    text_file = open(f'{json_path}_output.json', 'w')
    for element in result:
        text_file.write(element)
    text_file.close()

    print('\n', 'OUTPUT:', '\n \n', f'{output_list}' '\n')


if __name__ == '__main__':
    json_path = sys.argv[1]
    meds_json_formatter(json_path)

