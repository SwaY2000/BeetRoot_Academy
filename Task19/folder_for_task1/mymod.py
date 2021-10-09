class Testing_file:

    def __init__(self):
        self.answear = input("Hi! I'm test file, your file located in different folder?\n"
                        "Type \"Yes\" in different folder or \"No\" if same folder\n")
        if self.answear.lower() == "yes":
            self.way_file = input("Okay, you may type located like \n"
                            "\"C:/Users/Folder/file.name\"\n")

        elif self.answear.lower() == "no":
            self.way_file = input("Okay, type name file\n")

        else:
            print("Answear may be \"Yes\" or \"No\"")
            Testing_file().__init__()
        self.answear = input("So, i can return for you count lines, count chairs and together this function. \n"
                        "Type:\n"
                        "count lines: 1\n"
                        "count chairs: 2\n"
                        "together: 3\n")
        try:
            if self.answear == "1":
                self.way_file = str(Testing_file.__count_lines(self))
            elif self.answear == "2":
                self.way_filer = str(Testing_file.__count_chairs(self))
            elif self.answear == "3":
                self.way_file = str(Testing_file.__test(self))
            else:
                print("No such function")
                self.way_file = "File not found"
        except FileNotFoundError:
            self.way_file = "File not found"

    def __repr__(self):
        return self.way_file

    def __count_lines(self):
        with open(self.way_file) as file_n:
            return len(file_n.readlines())

    def __count_chairs(self):
        with open(self.way_file) as file_n:
            counting_chairs = 0
            for _ in range(self.__count_lines()):
                    counting_chairs += len(file_n.read())
            return counting_chairs

    def __test(self):
        return (self.__count_lines(), self.__count_chairs())


a = Testing_file()
print(a)
