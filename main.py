import sys
import subprocess
from PyQt5 import QtCore, QtWidgets
from magic import main as do_magic


class CardScraperApp(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Card Scraper")
        self.init_ui()

    def init_ui(self):
        self.start_button = QtWidgets.QPushButton("Start Scraper")
        self.loading_label = QtWidgets.QLabel()

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.start_button)
        layout.addWidget(self.loading_label)

        self.setLayout(layout)

        self.start_button.clicked.connect(self.run_scraper)

    def run_scraper(self):
        self.start_button.setEnabled(False)
        self.loading_label.setText("Loading...")

        try:
            do_magic()
            self.loading_label.setText("Complete")
        except subprocess.CalledProcessError:
            self.loading_label.setText("Error occurred")

        self.start_button.setEnabled(True)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = CardScraperApp()
    window.show()
    sys.exit(app.exec_())
