import json
from itertools import chain
import requests


# json_file_path = 'output.json'

# # Read and load the JSON file
# with open(json_file_path, 'r') as json_file:
#     data = json.load(json_file)

# dates = []
# vals = []

# date = data.keys()
# val = data.values()


# # print(dates.sort())
# dates.append(sorted(date))
# vals.append(sorted(val))


# flattened_dates = list(chain.from_iterable(dates))
# flattened_values = list(chain.from_iterable(vals))

# print( flattened_dates)
# print( flattened_values)

# data_dict = {str(date): str(value) for date, value in zip(flattened_dates, flattened_values) if date is not None}
# with open('output4.json', 'w') as json_file:
#     json.dump(data_dict, json_file, indent=2)

# def checkFileExists(fileID):
#     url = 'https://links.sgx.com/1.0.0/derivatives-historical/' + str(fileID) + '/TC.txt'
#     response = requests.head(url, allow_redirects=False)
#     if response.status_code == 302:
#         print("File not Found")
#     else:
#         print("file exists")

# checkFileExists(5602)

# arr1 = ['20040723']
# arr2 = [5599]
# arr3 = ['WEBPXTICK_DT.zip', 'TickData_structure.dat', 'TC.txt', 'TC_structure.dat']

# # Creating the JSON structure
# result_json = {arr1[0]: {arr2[0]: {arr3[i].split('.')[0]: f'{arr3[i].split(".")[0]}-20240122.{arr3[i].split(".")[1]}' if i == 0 else arr3[i].replace(".txt", f"_20240122.{arr3[i].split('.')[1]}") for i in range(len(arr3))}}}

# with open('output5.json', 'w') as json_file:
#     json.dump(result_json, json_file, indent=2)

arr1 = ['20040723', '20040722']
arr2 = [5599, 5598]
arr3 = ['WEBPXTICK_DT-20240123.zip', 'TickData_structure.dat', 'TC_20240123.txt', 'TC_structure.dat', 'WEBPXTICK_DT-20240122.zip', 'TickData_structure.dat', 'TC_20240122.txt', 'TC_structure.dat']

result_dict = {}

for date, code, file in zip(arr1, arr2, arr3):
    if date not in result_dict:
        result_dict[date] = {}

    if code not in result_dict[date]:
        result_dict[date][code] = {}

    key = file.split('_')[0]
    result_dict[date][code][key] = file

result_json = json.dumps(result_dict, indent=4)
print(result_json)



# Print the resulting JSON
# with open('output6.json', 'w') as json_file:
#     json.dump(result_json, json_file, indent=2)
# print(result_json)
