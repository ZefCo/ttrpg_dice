import os
import json
# import pandas

def load_json(file_path):
    with open(file_path, 'r') as json_file:
        j = json.load(json_file)
    return j

def write_json(file_path, data_dump):
    with open(file_path, 'w+') as json_file:
        json.dump(data_dump, json_file, indent=6)

def write_txt(file_path, data_dump):
    with open(file_path, 'w+') as txt_file:
        txt_file.write(data_dump)

def subdirectory_file_path(file):
    cwd = os.getcwd()
    path = os.path.join(cwd, file)
    return path

def read_txt(file_path):
    with open(file_path, 'r') as txt_file:
        txt_dump = txt_file.readlines()
        # pass
    return txt_dump

# def txt_2_csv(file_path):
#     with open(file_path, 'r') as txt_file:
#         txt_dump = txt_file.readlines()
    


def main():
    cwd = os.getcwd()
    file_path = os.path.join(cwd, 'RNA_Protein.json')
    json = load_json(file_path)
    print(json['UUU'])
    # j = File(file_path)
    # j.load_json(j.file_path)
    # print(j.json_data)
    # # pass

if __name__ in '__main__':
    main()