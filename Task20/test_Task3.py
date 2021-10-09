import pytest

import Task3
class TestPyTest:
    @staticmethod
    def test_open():
        with pytest.raises(FileNotFoundError):
            Task3.CensoredWords("tesk.txt", "Python")


class CensoredWords(TestPyTest):
    def __init__(self, path_file, delete_w):
        TestPyTest.test_open()
        try:
            with open(path_file, "r") as self.fr:
                self.fr = self.fr.read()
                self.delete_words(delete_w, path_file)
        except FileNotFoundError:
            raise FileNotFoundError

    def delete_words(self, delete_w, path_file):
        if delete_w in self.fr:
            with open(path_file, "w") as self.fw:
                self.fw.write(self.fr.replace(delete_w, "CENSORED"))

a = CensoredWords("test.txt", "Python")






if __name__ == "__main__":
    TestPyTest.test_open()