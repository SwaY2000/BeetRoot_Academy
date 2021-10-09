
class CensoredWords:
    def __init__(self, path_file, delete_w):
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
