from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QWidget, \
    QSlider, QDoubleSpinBox
from PyQt6.QtGui import QIcon, QPixmap, QFont
from PyQt6.QtCore import QSize, Qt
import sys
from кости import *


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("DICE")
        self.setWindowIcon(QIcon('Dice-logo.png'))
        self.setFixedSize(QSize(700, 500))
        font = QFont("Arial Rounded MT Bold", 15)

        self.button_more = QPushButton("MORE")
        self.button_more.setFont(font)
        self.button_more.clicked.connect(self.the_button_was_clicked)

        self.button_less = QPushButton("LESS")
        self.button_less.setFont(font)
        self.button_less.clicked.connect(self.the_button_was_clicked)

        self.bet_value = QDoubleSpinBox()
        self.bet_value.setFixedSize(150, 50)
        self.bet_value.setFont(font)
        self.bet_value.setMinimum(1)

        self.result = QLabel()
        self.result.setFont(font)
        self.result.setStyleSheet("color: white;")

        self.chance = QSlider(Qt.Orientation.Horizontal)
        self.chance.setValue(50)
        self.chance.setMinimum(1)
        self.chance.setMaximum(95)
        self.chance.setStyleSheet("color: white;")

        self.chance.valueChanged.connect(self.chance_changed)

        self.chance_value = QLabel("50")
        self.chance_value.setFont(font)
        self.chance_value.setStyleSheet("color: white;")

        layout = QVBoxLayout()

        layout_1 = QHBoxLayout()
        layout_1.addWidget(self.button_more)
        layout_1.addWidget(self.button_less)
        layout_1.setSpacing(0)

        layout_2 = QHBoxLayout()
        layout_2.addWidget(self.chance)
        layout_2.addWidget(self.chance_value)
        layout_2.setSpacing(10)
        layout_2.setContentsMargins(50, 200, 50, 0)

        layout_3 = QHBoxLayout()
        layout_3.addWidget(self.bet_value)
        layout_3.setContentsMargins(0, 100, 500, 0)

        layout.addLayout(layout_3)
        layout.addLayout(layout_2)
        layout.addLayout(layout_1)

        container = QWidget()
        container.setLayout(layout)

        self.setCentralWidget(container)

    def the_button_was_clicked(self):
        pass

    def chance_changed(self):
        self.chance_value.setText(str(self.chance.value()))


app = QApplication(sys.argv)
window = MainWindow()
window.setObjectName("MainWindow")
window.setStyleSheet("#MainWindow{background-color:black}")
window.show()
sys.exit(app.exec())
