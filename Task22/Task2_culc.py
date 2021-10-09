import sys

from PySide6.QtWidgets import QApplication, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QDialog, QLineEdit

class Widget_culc(QPushButton, QLabel, QHBoxLayout, QVBoxLayout, QDialog, QLineEdit):

    def __init__(self):
        super(Widget_culc, self).__init__()
        self.second_digit = False
        self.first_num = ""
        self.second_num = ""
        self.widget()

    def widget(self):

        self.window_show = QLabel("")
        self.horizontal_main = QHBoxLayout()
        self.horizontal_main.addWidget(self.window_show)

        self.one = QPushButton("1")
        self.one.clicked.connect(lambda: self.logic(1))
        self.two = QPushButton("2")
        self.two.clicked.connect(lambda: self.logic(2))
        self.three = QPushButton("3")
        self.three.clicked.connect(lambda: self.logic(3))

        self.horizontal_one = QHBoxLayout()
        self.horizontal_one.addWidget(self.one)
        self.horizontal_one.addWidget(self.two)
        self.horizontal_one.addWidget(self.three)

        self.four = QPushButton("4")
        self.four.clicked.connect(lambda: self.logic(4))
        self.five = QPushButton("5")
        self.five.clicked.connect(lambda: self.logic(5))
        self.six = QPushButton("6")
        self.six.clicked.connect(lambda: self.logic(6))

        self.horizontal_two = QHBoxLayout()
        self.horizontal_two.addWidget(self.four)
        self.horizontal_two.addWidget(self.five)
        self.horizontal_two.addWidget(self.six)

        self.seven = QPushButton("7")
        self.seven.clicked.connect(lambda: self.logic(7))
        self.eight = QPushButton("8")
        self.eight.clicked.connect(lambda: self.logic(8))
        self.nine = QPushButton("9")
        self.nine.clicked.connect(lambda: self.logic(9))

        self.horizontal_three = QHBoxLayout()
        self.horizontal_three.addWidget(self.seven)
        self.horizontal_three.addWidget(self.eight)
        self.horizontal_three.addWidget(self.nine)

        self.zero = QPushButton("0")
        self.zero.clicked.connect(lambda: self.logic(3))
        self.point = QPushButton(".")
        self.answear = QPushButton("=")
        self.answear.clicked.connect(self.answear_num)

        self.horizontal_four = QHBoxLayout()
        self.horizontal_four.addWidget(self.zero)
        self.horizontal_four.addWidget(self.point)
        self.horizontal_four.addWidget(self.answear)

        self.plus = QPushButton("+")
        self.plus.clicked.connect(lambda: self.unar("+"))
        self.minus = QPushButton("-")
        self.minus.clicked.connect(lambda: self.unar("-"))
        self.multiply = QPushButton("*")
        self.multiply.clicked.connect(lambda: self.unar("*"))
        self.division = QPushButton("/")
        self.division.clicked.connect(lambda: self.unar("/"))

        self.vertical_unar = QVBoxLayout()
        self.vertical_unar.addWidget(self.plus)
        self.vertical_unar.addWidget(self.minus)
        self.vertical_unar.addWidget(self.multiply)
        self.vertical_unar.addWidget(self.division)

        self.layout = QVBoxLayout()


        self.layout.addLayout(self.horizontal_main)
        self.layout.addLayout(self.horizontal_one)
        self.layout.addLayout(self.horizontal_two)
        self.layout.addLayout(self.horizontal_three)
        self.layout.addLayout(self.horizontal_four)
        self.layout.addLayout(self.vertical_unar)

        self.setLayout(self.layout)

    def logic(self, num: int):
        if self.second_digit is False:
            self.first_num += str(num)

            self.horizontal_main.removeWidget(self.window_show)
            self.window_show.deleteLater()
            self.window_show = None

            self.window_show = QLabel(self.first_num)
            self.horizontal_main.addWidget(self.window_show)

        elif self.second_digit is True:
            self.second_num += str(num)

            self.horizontal_main.removeWidget(self.window_show)
            self.window_show.deleteLater()
            self.window_show = None

            self.window_show = QLabel(self.first_num+self.unar_symbol+self.second_num)
            self.horizontal_main.addWidget(self.window_show)

    def unar(self, unar_symbol: str):
        self.unar_symbol = unar_symbol
        self.second_digit = True

        self.horizontal_main.removeWidget(self.window_show)
        self.window_show.deleteLater()
        self.window_show = None

        self.window_show = QLabel(str(self.first_num) + self.unar_symbol)
        self.horizontal_main.addWidget(self.window_show)

    def answear_num(self):
        self.horizontal_main.removeWidget(self.window_show)
        self.window_show.deleteLater()
        self.window_show = None
        if self.unar_symbol == "+":
            self.window_show = QLabel(str(int(self.first_num) + int(self.second_num)))
        elif self.unar_symbol == "-":
            self.window_show = QLabel(str(int(self.first_num) - int(self.second_num)))
        elif self.unar_symbol == "*":
            self.window_show = QLabel(str(int(self.first_num) * int(self.second_num)))
        elif self.unar_symbol == "/":
            self.window_show = QLabel(str(int(self.first_num) / int(self.second_num)))
        self.horizontal_main.addWidget(self.window_show)


if __name__ == "__main__":
    app = QApplication()
    widget = Widget_culc()
    widget.show()
    app.exec()