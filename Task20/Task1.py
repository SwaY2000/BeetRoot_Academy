import logging
from os import path

class FalseOpen: #Like False Dmitry

    counting = 0

    def __init__(self, path_file, mode):
        logging.debug('You must getting all parameters and thay must be right')

        if path.isfile(path_file) is False:
            logging.warning(f'Parameter path_file: {path_file} is not file')
            raise FileNotFoundError
        if mode not in ['r', "r+", 'w', "w+", 'a', 'x']:
            logging.warning(f'Parameter mode: {path_file} unsupported')
            raise ValueError

        self.path_file = path_file
        self. mode = mode

    @classmethod
    def __counter(cls):
        cls.counting += 1
        return cls.counting

    def __enter__(self):
        FalseOpen.__counter()
        self.open_file = open(self.path_file, self.mode)
        print(f'Inside in __enter__. Counting: {self.counting}')
        return self.open_file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.open_file.close()
        print('Inside in __exit__')

if __name__ == '__main__':
    with FalseOpen('test.txt', 'r') as f:
        print(f.read())