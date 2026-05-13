# Nama: Deswita Salsabila
# NIM: F1D02410004
# Kelas: C

import sys
import requests
import threading
from PySide6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QPushButton, QMessageBox,
    QTableWidget, QTableWidgetItem, QLabel, QLineEdit
)


class PostManager(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Post Manager")
        self.resize(800, 500)

        layout = QVBoxLayout()

        self.label = QLabel("Post Manager")
        layout.addWidget(self.label)

        self.table = QTableWidget()
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(["ID", "Title", "Author", "Status"])
        layout.addWidget(self.table)

        self.btn_load = QPushButton("Load Data")
        layout.addWidget(self.btn_load)

        self.input_title = QLineEdit()
        self.input_title.setPlaceholderText("Title")
        layout.addWidget(self.input_title)
        
        self.input_body = QLineEdit()
        self.input_body.setPlaceholderText("Body")
        layout.addWidget(self.input_body)
        
        self.input_author = QLineEdit()
        self.input_author.setPlaceholderText("Author")
        layout.addWidget(self.input_author)
        
        self.input_slug = QLineEdit()
        self.input_slug.setPlaceholderText("Slug (HARUS UNIK)")
        layout.addWidget(self.input_slug)
        
        self.input_status = QLineEdit()
        self.input_status.setPlaceholderText("Status (published/draft)")
        layout.addWidget(self.input_status)

        self.btn_add = QPushButton("Tambah Data")
        layout.addWidget(self.btn_add)

        self.detail_label = QLabel("Detail Post:")
        layout.addWidget(self.detail_label)

        self.selected_id = None

        self.btn_edit = QPushButton("Edit Data")
        layout.addWidget(self.btn_edit)

        self.btn_delete = QPushButton("Hapus Data")
        layout.addWidget(self.btn_delete)

        self.status_label = QLabel("")
        layout.addWidget(self.status_label)

        self.setLayout(layout)

        self.btn_load.clicked.connect(self.load_data_thread)
        self.btn_add.clicked.connect(self.add_data_thread)
        self.table.cellClicked.connect(self.show_detail)
        self.table.cellClicked.connect(self.get_selected_row)
        self.btn_edit.clicked.connect(self.edit_data_thread)
        self.btn_delete.clicked.connect(self.delete_data_thread)

    def load_data(self):
        self.status_label.setText("Loading...")
        
        url = "https://api.pahrul.my.id/api/posts"
        
        try:
            response = requests.get(url)
            result = response.json()
            
            posts = result["data"]
            self.posts = posts

            self.table.setRowCount(0)

            for row, post in enumerate(posts):
                self.table.insertRow(row)
                self.table.setItem(row, 0, QTableWidgetItem(str(post["id"])))
                self.table.setItem(row, 1, QTableWidgetItem(post["title"]))
                self.table.setItem(row, 2, QTableWidgetItem(post["author"]))
                self.table.setItem(row, 3, QTableWidgetItem(post["status"]))

            self.status_label.setText("Selesai ✅")

        except Exception as e:
            self.status_label.setText("Error ❌")
            print("Error:", e)

    def add_data(self):
        url = "https://api.pahrul.my.id/api/posts"
        
        data = {
            "title": self.input_title.text(),
            "body": self.input_body.text(),
            "author": self.input_author.text(),
            "slug": self.input_slug.text(),
            "status": self.input_status.text()
        }
        
        try:
            response = requests.post(url, json=data)
            result = response.json()
            self.status_label.setText("Data berhasil ditambahkan!")
            print(result)
            
            self.load_data()
            
        except Exception as e:
            print("Error:", e)
            self.input_title.clear()
            self.input_body.clear()
            self.input_author.clear()
            self.input_slug.clear()
            self.input_status.clear()

    def show_detail(self, row, column):
        post = self.posts[row]
        
        comments_text = ""
        if "comments" in post:
            for c in post["comments"]:
                comments_text += f"- {c['comment']}\n"

        detail_text = f"""
    Title: {post['title']}
    Body: {post['body']}
    Author: {post['author']}
    Slug: {post['slug']}
    Status: {post['status']}

    Comments:
    {comments_text if comments_text else 'Tidak ada komentar'}
  """
        self.detail_label.setText(detail_text)

    def get_selected_row(self, row, column):
        self.selected_id = self.table.item(row, 0).text()
        self.input_title.setText(self.table.item(row, 1).text())
        self.input_author.setText(self.table.item(row, 2).text())
        self.input_status.setText(self.table.item(row, 3).text())

    def edit_data(self):
        if not self.selected_id:
            print("Pilih data dulu!")
            return
        
        url = f"https://api.pahrul.my.id/api/posts/{self.selected_id}"
        
        data = {
            "title": self.input_title.text(),
            "body": self.input_body.text(),
            "author": self.input_author.text(),
            "slug": self.input_slug.text(),
            "status": self.input_status.text()
        }
        
        try:
            response = requests.put(url, json=data)
            result = response.json()

            QMessageBox.information(self, "Sukses", "Data berhasil diupdate!")
           
            self.load_data()
            
        except Exception as e:
            QMessageBox.critical(self, "Error", "Gagal update data!")
            print("Error:", e)

    def delete_data(self):
        if not self.selected_id:
            print("Pilih data dulu!")
            return
        
        reply = QMessageBox.question(
            self,
            "Konfirmasi",
            "Yakin ingin menghapus data ini?",
            QMessageBox.Yes | QMessageBox.No
            
        )
        
        if reply == QMessageBox.No:
            return
        
        url = f"https://api.pahrul.my.id/api/posts/{self.selected_id}"
        
        try:
            response = requests.delete(url)
            result = response.json()
            print("Berhasil dihapus:", result)
            self.load_data()
        
        except Exception as e:
            print("Error:", e)

    def load_data_thread(self):
        thread = threading.Thread(target=self.load_data)
        thread.start()

    def add_data_thread(self):
        thread = threading.Thread(target=self.add_data)
        thread.start()

    def edit_data_thread(self):
        thread = threading.Thread(target=self.edit_data)
        thread.start()

    def delete_data_thread(self):
        thread = threading.Thread(target=self.delete_data)
        thread.start()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PostManager()
    window.show()
    sys.exit(app.exec())