import sys
import subprocess
import os
from PyQt5 import QtCore, QtWidgets, QtGui
from magic import main as do_magic


class ScraperThread(QtCore.QThread):
    finished = QtCore.pyqtSignal()
    error = QtCore.pyqtSignal()

    def run(self):
        try:
            do_magic()
            self.finished.emit()
        except subprocess.CalledProcessError:
            self.error.emit()


class CardScraperApp(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("𝘾𝘼𝙍𝘿𝙎𝘾𝙍𝘼𝙋𝙀𝙍")

        # Hide window title icon
        self.setWindowFlags(QtCore.Qt.WindowTitleHint | QtCore.Qt.CustomizeWindowHint)

        # Set window size
        screen_size = QtWidgets.QDesktopWidget().screenGeometry(-1)
        desired_width = screen_size.width() * 3 // 10
        desired_height = screen_size.height() * 3 // 10
        self.resize(desired_width, desired_height)

        self.init_ui()

    def init_ui(self):
        # Main Program Title
        self.thank_you_label = QtWidgets.QLabel("<center>𝕿𝖊𝖓𝖙𝖍𝖕𝖗𝖎𝖓𝖈𝖊<br />ⓒⓐⓡⓓⓢⓒⓡⓐⓟⓔⓡ</center>")

        # Button to activate scrape program
        self.url_button = QtWidgets.QPushButton("Enter URLs")

        # Button to activate scrape program
        self.start_button = QtWidgets.QPushButton("Start Scraper")

        # Loading text
        self.loading_label = QtWidgets.QLabel()

        # Open Generated CSV (set to be disabled and hidden on start)
        self.open_csv_button = QtWidgets.QPushButton("Open CSV")
        self.open_csv_button.setEnabled(False)
        self.open_csv_button.hide()

        # Close Program button (Originally was set to be disabled until program ran, I changed it)
        self.close_button = QtWidgets.QPushButton("Close")
        self.close_button.setEnabled(True)

        # Define Layout for window and each widget
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.thank_you_label, alignment=QtCore.Qt.AlignCenter)
        layout.addWidget(self.url_button, alignment=QtCore.Qt.AlignCenter)
        layout.addWidget(self.start_button, alignment=QtCore.Qt.AlignCenter)
        layout.addWidget(self.loading_label, alignment=QtCore.Qt.AlignCenter)
        layout.addWidget(self.open_csv_button, alignment=QtCore.Qt.AlignCenter)
        layout.addWidget(self.close_button, alignment=QtCore.Qt.AlignCenter)

        self.setLayout(layout)

        # Connect Clicking buttons to specified actions
        self.start_button.clicked.connect(self.run_scraper)
        self.url_button.clicked.connect(self.open_url_file)
        self.close_button.clicked.connect(self.close_application)
        self.open_csv_button.clicked.connect(self.open_csv_file)

        # Connect to scraper thread and tell when it is complete or if error occurred
        self.scraper_thread = ScraperThread()
        self.scraper_thread.finished.connect(self.scraper_finished)
        self.scraper_thread.error.connect(self.scraper_error)

        # Set font properties
        # General font properties
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(9)

        # Main Program Title font properties
        thank_you_font = QtGui.QFont()
        thank_you_font.setFamily("Verdana")
        thank_you_font.setPointSize(15)

        # Connect fonts to widget items
        self.start_button.setFont(font)
        self.loading_label.setFont(font)
        self.close_button.setFont(font)
        self.open_csv_button.setFont(font)
        self.thank_you_label.setFont(thank_you_font)

    def run_scraper(self):
        self.start_button.setEnabled(False)
        self.close_button.setEnabled(True)
        self.loading_label.setText("Loading... Please wait...")

        self.scraper_thread.start()

    def scraper_finished(self):
        self.loading_label.setText("Output successful to card_prices.csv")
        self.start_button.setEnabled(True)
        self.close_button.setEnabled(True)
        self.open_csv_button.setEnabled(True)
        self.open_csv_button.show()

    def scraper_error(self):
        self.loading_label.setText("Error occurred")
        self.start_button.setEnabled(True)
        self.close_button.setEnabled(True)
        self.open_csv_button.setEnabled(False)

    def close_application(self):
        QtWidgets.QApplication.quit()

    def open_csv_file(self):
        current_dir = os.getcwd()
        csv_file_path = os.path.join(current_dir, "card_prices.csv")
        if os.path.isfile(csv_file_path):
            os.startfile(csv_file_path)

    def open_url_file(self):
        current_dir = os.getcwd()
        url_file_path = os.path.join(current_dir, "cardlist.csv")
        if os.path.isfile(url_file_path):
            os.startfile(url_file_path)

    def paintEvent(self, event):

        # Set background color
        bg_color = QtGui.QColor("#000000")
        painter = QtGui.QPainter(self)
        painter.setBrush(bg_color)
        painter.drawRect(self.rect())

        # Set text color
        text_color = QtGui.QColor("#ff9900")
        self.start_button.setStyleSheet("color: {0}".format(text_color.name()))
        self.url_button.setStyleSheet("color: {0}".format(text_color.name()))
        self.loading_label.setStyleSheet("color: {0}".format(text_color.name()))
        self.close_button.setStyleSheet("color: {0}".format(text_color.name()))
        self.open_csv_button.setStyleSheet("color: {0}".format(text_color.name()))
        self.thank_you_label.setStyleSheet("color: {0}".format(text_color.name()))

        # Set button colors
        button_bg_color = QtGui.QColor("#4d2800")
        button_text_color = QtGui.QColor("#ff9900")
        button_style = "background-color: {0}; color: {1};".format(button_bg_color.name(), button_text_color.name())
        self.start_button.setStyleSheet(button_style)
        self.close_button.setStyleSheet(button_style)
        self.url_button.setStyleSheet(button_style)
        self.open_csv_button.setStyleSheet(button_style)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = CardScraperApp()
    window.show()
    sys.exit(app.exec_())
