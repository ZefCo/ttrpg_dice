import os
import json

class File():
    def __init__(self, file_path) -> None:
        self.file_path = file_path
        # self.load_file(self.file_path)

    def load_json(self, file_path):
        with open(file_path, 'r') as json_file:
            setattr(self, 'json_data', json.load(json_file))


def main():
    cwd = os.getcwd()
    file_path = os.path.join(cwd, 'JSONS','standard_dice.json')
    j = File(file_path)
    j.load_json(j.file_path)
    print(j.json_data)
    # pass

if __name__ in '__main__':
    main()