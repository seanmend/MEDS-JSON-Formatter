import sys
import json


# pass csv when calling. ex:python3 main.py file.csv
def meds_json_formatter(json_path):
    output_list = []
    if not json_path:
        raise RuntimeError
    # print(json_path)
    # Opening JSON file
    f = open(json_path, )

    # returns JSON object as
    # a dictionary
    data = json.load(f)

    # count = 0
    #
    values = data.values()
    # for v in values:
    #     count += 1
    keys = data.keys()
    # print('keys: ', keys)
    # print(keys)
    # print('-------------------')
    # print('values: ', values)
    length_of_list = len(keys)
    # print(length_of_list)

    # Format existing

    for i in range(1, length_of_list + 1):
        # print('loop')
        first_key = list(data)[i - 1]
        first_val = list(data.values())[i - 1]
        output_list.append({"code": first_key, "item": first_val})

    # Add New Entry
    new_key = '1734'  # EDIT
    new_val = 'Non Medicaid Florida Community Care'  # EDIT
    output_list.append({"code": new_key, "item": new_val})

    # print('OUTPUT:', output_list)







    # print(data)

    # with open(json_path, 'r+') as file:
    #     # First we load existing data into a dict.
    #     file_data = json.load(file)
    #     # Join new_data with file_data inside emp_details
    #     file_data[x].append(new_data)
    #     # Sets file's current position at offset.
    #     file.seek(0)
    #     # convert back to json.
    #     json.dump(file_data, file, indent=4)


# python object to be appended
# y = {"emp_name": "Nikhil",
#      "email": "nikhil@geeksforgeeks.org",
#      "job_profile": "Full Time"
#      }
#
# write_json(y)






    # count = 0
    #
    values = data.values()
    # for v in values:
    #     count += 1
    keys = data.keys()
    # print('keys: ', keys)
    # print(keys.type())
    # print('-------------------')
    # print('values: ', values)

    # length_of_list = len(keys)
    # print(length_of_list)

    # for n in range(count):
    #     print('n:::', n)
    #     output_list.append({"code": keys[n], "item": values[n]})
    #     json.dump(data, file, indent=4)
    #
    # print('output::::', output_list)

    #
    # for l in length_of_list:
    #     output.append(l)

    # for x in data:
    #     print(data[x])

    # output = [{"code": keys, "item": values} ]
    # print(output)

    # output_list = dict(zip(keys, values))

    # for key in keys:
    #     print('v:::::', value)
    #     output_list.append({key, value})
    #
    # for value in values:
    #     print('v:::::', value)
    #     output_list.append({key, value})

    # print('OUTPUT:::::::::::::::::::::::::')
    # print(output_list)
    # # Closing file
    # f.close()











    # Iterating through the json
    # list
    # values = data.values()
    # keys = data.keys()
    # print('keys: ', keys)
    # print('-------------------')
    # print('values: ', values)
    #
    # output_list = []
    #
    # for key in keys:
    #     print('v:::::', value)
    #     output_list.append({key, value})
    #
    # for value in values:
    #     print('v:::::', value)
    #     output_list.append({key, value})
    #
    # print('OUTPUT:::::::::::::::::::::::::')
    # print(output_list)
    # # Closing file
    # f.close()

    # save output as text file

    # textfile = open("output.txt", "w")
    # for element in output_list:
    #     textfile.write(element)
    # textfile.close()










    result = json.dumps(output_list)

    # printing result as string
    print(type(result))
    print("final string = ", result)

    text_file = open('output.txt', 'w')
    for element in result:
        text_file.write(element)
    text_file.close()


if __name__ == '__main__':
    json_path = sys.argv[1]
    meds_json_formatter(json_path)

