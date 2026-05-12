import sys
from PySide6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QTableWidget,
    QPushButton
)

class PostManager(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Post Manager")
        self.resize(800, 500)

        layout = QVBoxLayout()

        self.table = QTableWidget()
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(["ID", "Title", "Author", "Status"])

        layout.addWidget(self.table)

        self.btn_load = QPushButton("Load Data")
        layout.addWidget(self.btn_load)

        self.setLayout(layout)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PostManager()
    window.show()
    sys.exit(app.exec())