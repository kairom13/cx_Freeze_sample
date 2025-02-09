"""A simple script to demonstrate PyQt5."""

import sys

print('\n\n\n\n\n\nImporting Packages')

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QLabel, QWidget


def main():
    print('Entered the Main Method')
    app = QApplication(sys.argv)
    window = QWidget()
    window.setWindowTitle("Simple")
    window.setGeometry(300, 300, 300, 300)
    label = QLabel(window)
    label.setText("Hello World!")
    label.setGeometry(0, 0, 300, 300)
    label.setAlignment(Qt.AlignCenter)
    window.show()
    return app.exec_()


if __name__ == "__main__":
    sys.exit(main())
