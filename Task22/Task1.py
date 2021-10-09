from Phonebook import phone_logic, phone_methods
import sys
from PySide6.QtWidgets import QApplication, QPushButton, QLabel, QVBoxLayout, QDialog, QLineEdit

class PhoneBook(QPushButton, QDialog):
    def __init__(self):
        super(PhoneBook, self).__init__()

        self.buttom_start = QPushButton("Start")
        self.buttom_start.clicked.connect(self.__start_program)
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.buttom_start)
        self.setLayout(self.layout)

    def __start_program(self):
        self.__remove_button(self.buttom_start)

        self.quest_text = QLabel("<h3>Choose function</h3>")

        self.button_search = QPushButton("Search contact")
        self.button_search.clicked.connect(self.__search)
        self.layout.addWidget(self.button_search)

        self.button_add = QPushButton("Add new contact")
        self.button_add.clicked.connect(self.__add)
        self.layout.addWidget(self.button_add)

        self.button_delete = QPushButton("Delete contact")
        self.button_delete.clicked.connect(self.__delete)
        self.layout.addWidget(self.button_delete)

        self.button_update = QPushButton("Update information contact")
        self.button_update.clicked.connect(self.__update)
        self.layout.addWidget(self.button_update)

    def __search(self):
        self.__remove_button(self.button_search, self.button_add, self.button_delete,
                             self.button_update, self.quest_text)

        self.quest_text = QLabel("<h3>Type number contact</h3>")
        self.button_action = QPushButton("Find")
        self.user_input = QLineEdit()

        self.layout.addWidget(self.quest_text)
        self.layout.addWidget(self.button_action)
        self.layout.addWidget(self.user_input)

        #I dont khow how fix autorun butto. Couse i create another function ;(
        self.button_action.clicked.connect(self.__click_search)



    def __click_search(self):
        try:
            self.info = phone_methods.search(self.user_input.text())
        except Exception:
            pass
        else:
            self.__remove_button(self.quest_text, self.button_action, self.user_input)

            self.num = QLabel(f"Number contact: {self.user_input.text()}")
            self.first_name = QLabel("First name: {0}".format(self.info["first_name"]))
            self.last_name = QLabel("Last name: {0}".format(self.info["last_name"]))
            self.city = QLabel("City: {0}".format(self.info["city"]))
            self.button_continue = QPushButton("Continue")
            self.button_continue.clicked.connect(self.__exit)

            self.layout.addWidget(self.num)
            self.layout.addWidget(self.first_name)
            self.layout.addWidget(self.last_name)
            self.layout.addWidget(self.city)
            self.layout.addWidget(self.button_continue)


    def __add(self):
        self.__remove_button(self.button_search, self.button_add, self.button_delete,
                             self.button_update, self.quest_text)

        self.info = QLabel("Type information")
        self.text_num = QLabel("Number")
        self.text_fn = QLabel("First name")
        self.text_ln = QLabel("Last name")
        self.text_city = QLabel("City")

        self.num = QLineEdit()
        self.first_name = QLineEdit()
        self.last_name = QLineEdit()
        self.city = QLineEdit()
        self.button_continue = QPushButton("Continue")

        self.layout.addWidget(self.info)
        self.layout.addWidget(self.text_num)
        self.layout.addWidget(self.num)
        self.layout.addWidget(self.text_fn)
        self.layout.addWidget(self.first_name)
        self.layout.addWidget(self.text_ln)
        self.layout.addWidget(self.last_name)
        self.layout.addWidget(self.text_city)
        self.layout.addWidget(self.city)
        self.layout.addWidget(self.button_continue)

        self.button_continue.clicked.connect(self.__click_add)

    def __click_add(self):
        try:
            phone_methods.add(self.num.text(), self.first_name.text(), self.last_name.text(), self.city.text())
        except Exception:
            print("Nope")
        else:
            self.__remove_button(self.info, self.text_num, self.text_fn, self.text_ln, self.text_city,
                                 self.num, self.first_name, self.last_name, self.city, self.button_continue)
            self.done = QLabel("Done")
            self.button_continue = QPushButton("Continue")

    def __delete(self):
        self.__remove_button(self.button_search, self.button_add, self.button_delete,
                             self.button_update, self.quest_text)

        self.info = QLabel("You want delete by:")
        self.num = QPushButton("Number")
        self.first_name = QPushButton("First name")
        self.last_name = QPushButton("Last name")
        self.fullname = QPushButton("Full name")

        self.layout.addWidget(self.info)
        self.layout.addWidget(self.num)
        self.layout.addWidget(self.first_name)
        self.layout.addWidget(self.last_name)
        self.layout.addWidget(self.fullname)

        self.num.clicked.connect(self.__num)
        self.first_name.clicked.connect(self.__first_name)
        self.last_name.clicked.connect(self.__last_name)
        self.fullname.clicked.connect(self.__fullname)

    def __num(self):
        self.__click_delete("num")
    def __first_name(self):
        self.__click_delete("first_name")
    def __last_name(self):
        self.__click_delete("last_name")
    def __fullname(self):
        self.__click_delete("fullname")

    def __click_delete(self, answear):
        self.__remove_button(self.info, self.num, self.first_name, self.last_name, self.fullname)
        if answear.lower() == "num":
            self.answear = "number"
        elif answear.lower() == "first_name":
            self.answear = "first name"
        elif answear.lower() == "last_name":
            self.answear = "last name"
        elif answear.lower() == "fullname":
            self.answear = "full name"
        self.info = QLabel(f"Input {self.answear}")
        self.info_del = QLineEdit()
        self.button_continue = QPushButton("Continue")

        self.layout.addWidget(self.info)
        self.layout.addWidget(self.info_del)
        self.layout.addWidget(self.button_continue)

        def run_continue():
            phone_methods.delete(self.answear, self.info_del)

        self.button_continue.clicked.connect(run_continue)



    def __update(self):
        pass

    def __remove_button(self, *args):
        """Remove from QtVBox widget from args """
        try:
            for i in args:
                self.layout.removeWidget(i)
                i.deleteLater()
                i = None
        except Exception:
            pass

    def __exit(self):
        self.__start_program()







if __name__ == '__main__':
    while True:
        app = QApplication(sys.argv)
        form = PhoneBook()
        form.show()
        app.exec()

