import sys
# from PyQt5.QtWidgets import *
# from PyQt5.QtCore import *
# from PyQt5 import *
import os
import fitz  # PyMuPDF
from PyQt6.QtWidgets import *
import sys


class BatchConversion(QMainWindow):
    def __init__(self):
        super().__init__()

        # set the title of main window
        self.setWindowTitle('PDF batch conversion')

        # set the size of window
        self.Width = 800
        self.height = int(0.618 * self.Width)
        self.resize(self.Width, self.height)
        # self.setGeometry(100, 100, 400, 400)

        # add all widgets
        self.btn_intro = QPushButton('Intro', self)
        self.btn_doc_to_pdf = QPushButton('doc to PDF', self)
        self.btn_txt_to_pdf = QPushButton('txt to PDF', self)
        self.btn_img_to_pdf = QPushButton('img to PDF', self)
        self.btn_pdf_to_txt = QPushButton('PDF to txt', self)
        self.btn_pdf_to_img = QPushButton('PDF to img', self)
        self.btn_split = QPushButton('Split', self)
        self.btn_merge = QPushButton('Merge', self)
        self.btn_password_protection = QPushButton('Password Protection', self)
        self.btn_remove_page = QPushButton('Remove Page', self)
        self.btn_watermark = QPushButton('Remove Page', self)
        self.btn_swap = QPushButton('Remove Page', self)

        self.btn_intro.clicked.connect(self.button_intro)
        self.btn_doc_to_pdf.clicked.connect(self.button_doc_to_pdf)
        self.btn_txt_to_pdf.clicked.connect(self.button_txt_to_pdf)
        self.btn_img_to_pdf.clicked.connect(self.button_img_to_pdf)
        self.btn_pdf_to_txt.clicked.connect(self.button_pdf_to_txt)
        self.btn_pdf_to_img.clicked.connect(self.button_pdf_to_img)
        self.btn_split.clicked.connect(self.button_split)
        self.btn_merge.clicked.connect(self.button_merge)
        self.btn_password_protection.clicked.connect(self.button_password_protection)
        self.btn_remove_page.clicked.connect(self.button_remove_page)
        self.btn_watermark.clicked.connect(self.button_watermark)
        self.btn_swap.clicked.connect(self.button_swap)

        # add tabs
        self.tab1 = self.ui1()
        self.tab2 = self.ui2()
        self.tab3 = self.ui3()
        self.tab4 = self.ui4()
        self.tab5 = self.ui5()
        self.tab6 = self.ui6()
        self.tab7 = self.ui7()
        self.tab8 = self.ui8()
        self.tab9 = self.ui9()
        self.tab10 = self.ui10()
        self.tab11 = self.ui11()

        self.initUI()

    def initUI(self):
        left_layout = QVBoxLayout()
        left_layout.addWidget(self.btn_intro)
        left_layout.addWidget(self.btn_doc_to_pdf)
        left_layout.addWidget(self.btn_txt_to_pdf)
        left_layout.addWidget(self.btn_img_to_pdf)
        left_layout.addWidget(self.btn_pdf_to_txt)
        left_layout.addWidget(self.btn_pdf_to_img)
        left_layout.addWidget(self.btn_split)
        left_layout.addWidget(self.btn_merge)
        left_layout.addWidget(self.btn_password_protection)
        left_layout.addWidget(self.btn_remove_page)
        left_layout.addWidget(self.btn_watermark)
        left_layout.addWidget(self.btn_swap)
        left_layout.addStretch(5)
        left_layout.setSpacing(20)
        left_widget = QWidget()
        left_widget.setLayout(left_layout)

        self.right_widget = QTabWidget()
        self.right_widget.tabBar().setObjectName("mainTab")

        self.right_widget.addTab(self.tab1, '')
        self.right_widget.addTab(self.tab2, '')
        self.right_widget.addTab(self.tab3, '')
        self.right_widget.addTab(self.tab4, '')
        self.right_widget.addTab(self.tab5, '')
        self.right_widget.addTab(self.tab6, '')
        self.right_widget.addTab(self.tab7, '')
        self.right_widget.addTab(self.tab8, '')
        self.right_widget.addTab(self.tab9, '')
        self.right_widget.addTab(self.tab10, '')
        self.right_widget.addTab(self.tab11, '')

        self.right_widget.setCurrentIndex(0)
        self.right_widget.setStyleSheet('''QTabBar::tab{width: 0; \
            height: 0; margin: 0; padding: 0; border: none;}''')

        main_layout = QHBoxLayout()
        main_layout.addWidget(left_widget)
        main_layout.addWidget(self.right_widget)
        main_layout.setStretch(0, 40)
        main_layout.setStretch(1, 200)
        main_widget = QWidget()
        main_widget.setLayout(main_layout)
        self.setCentralWidget(main_widget)

    # ----------------- 
    # buttons

    def button_intro(self):
        self.right_widget.setCurrentIndex(0)

    def button_doc_to_pdf(self):
        self.right_widget.setCurrentIndex(1)

    def button_txt_to_pdf(self):
        self.right_widget.setCurrentIndex(2)

    def button_img_to_pdf(self):
        self.right_widget.setCurrentIndex(3)

    def button_pdf_to_txt(self):
        self.right_widget.setCurrentIndex(4)

    def button_pdf_to_img(self):
        self.right_widget.setCurrentIndex(5)

    def button_split(self):
        self.right_widget.setCurrentIndex(6)

    def button_merge(self):
        self.right_widget.setCurrentIndex(7)

    def button_password_protection(self):
        self.right_widget.setCurrentIndex(8)

    def button_remove_page(self):
        self.right_widget.setCurrentIndex(9)

    def button_watermark(self):
        self.right_widget.setCurrentIndex(10)

    def button_swap(self):
        self.right_widget.setCurrentIndex(11)

    # ----------------- 
    # pages
    def ui1(self):
        main_layout = QVBoxLayout()
        main_layout.addWidget(QLabel('page 1'))
        main_layout.addStretch(5)
        main = QWidget()
        main.setLayout(main_layout)
        return main

    def ui2(self):
        main_layout = QVBoxLayout()
        main_layout.addWidget(QLabel('page 2'))
        main_layout.addStretch(5)
        main = QWidget()
        main.setLayout(main_layout)
        return main

    def ui3(self):
        main_layout = QVBoxLayout()
        main_layout.addWidget(QLabel('page 3'))
        main_layout.addStretch(5)
        main = QWidget()
        main.setLayout(main_layout)
        return main

    def ui4(self):
        # Layout
        main_layout = QVBoxLayout()

        # file List
        self.filename_list = QListWidget()
        main_layout.addWidget(self.filename_list)

        # Add file Section
        add_layout = QHBoxLayout()
        self.todo_input = QLineEdit()
        add_layout.addWidget(self.todo_input)
        add_button = QPushButton('Select')
        add_button.clicked.connect(self.add_todo)
        add_layout.addWidget(add_button)
        main_layout.addLayout(add_layout)

        # Select Folder Section
        folder_layout = QHBoxLayout()
        self.folder_input = QLineEdit()
        self.folder_input.setReadOnly(True)
        folder_layout.addWidget(self.folder_input)
        folder_button = QPushButton('Select Folder')
        folder_button.clicked.connect(self.select_folder)
        folder_layout.addWidget(folder_button)
        main_layout.addLayout(folder_layout)

        # Remove Todo Section
        remove_button = QPushButton('Remove')
        remove_button.clicked.connect(self.remove_todo)
        main_layout.addWidget(remove_button)

        



        # main_layout.addWidget(QLabel('page 1'))
        # main_layout.addStretch(5)
        main = QWidget()
        main.setLayout(main_layout)
        return main


    def ui5(self):
        main_layout = QVBoxLayout()
        main_layout.addWidget(QLabel('page 5'))
        main_layout.addStretch(5)
        main = QWidget()
        main.setLayout(main_layout)
        return main


    def ui6(self):
        main_layout = QVBoxLayout()
        main_layout.addWidget(QLabel('page 6'))
        main_layout.addStretch(5)
        main = QWidget()
        main.setLayout(main_layout)
        return main

    def ui7(self):
        main_layout = QVBoxLayout()
        main_layout.addWidget(QLabel('page 7'))
        main_layout.addStretch(5)
        main = QWidget()
        main.setLayout(main_layout)
        return main

    def ui8(self):
        main_layout = QVBoxLayout()
        main_layout.addWidget(QLabel('page 8'))
        main_layout.addStretch(5)
        main = QWidget()
        main.setLayout(main_layout)
        return main

    def ui9(self):
        main_layout = QVBoxLayout()
        main_layout.addWidget(QLabel('page 9'))
        main_layout.addStretch(5)
        main = QWidget()
        main.setLayout(main_layout)
        return main

    def ui10(self):
        main_layout = QVBoxLayout()
        main_layout.addWidget(QLabel('page 10'))
        main_layout.addStretch(5)
        main = QWidget()
        main.setLayout(main_layout)
        return main

    def ui11(self):
        main_layout = QVBoxLayout()
        main_layout.addWidget(QLabel('page 11'))
        main_layout.addStretch(5)
        main = QWidget()
        main.setLayout(main_layout)
        return main




    def select_folder(self):
        folder_path = QFileDialog.getExistingDirectory(self, 'Select Folder')

        if folder_path:
            self.folder_input.setText(folder_path)
            filename_list = self.access_files(folder_path)
            print(filename_list)
            self.pdf2txt(filename_list)

        else:
            QMessageBox.warning(self, 'Warning', 'Please enter a todo item.')

    def access_files(self, folder_path):
        if os.path.isdir(folder_path):  # Check if it's a valid directory
            filename_list = []
            for root, dirs, files in os.walk(folder_path):
                for filename in files:
                    filepath = os.path.join(root, filename)
                    filetype = filename[-3:]

                    # Do something with each file
                    # self.filename_list.addItem(filepath)
                    # self.filename_list.addItem(filename)
                    filename_list.append([filename[:-4], filepath, filetype])
                    # print(filename)  # Example: Print the filename
                    # with open(filepath, 'r') as f:  # Example: Open for reading
                    #     file_content = f.read()
                        # Process file content...
            return filename_list
        else:
            print("Error: Invalid folder path.")

    def add_todo(self):
        todo = self.todo_input.text()
        if todo:
            self.filename_list.addItem(todo)
            self.todo_input.clear()
        else:
            QMessageBox.warning(self, 'Warning', 'Please enter a todo item.')

    def remove_todo(self):
        selected_item = self.filename_list.currentItem()
        if selected_item:
            self.filename_list.takeItem(self.filename_list.row(selected_item))
        else:
            QMessageBox.warning(self, 'Warning', 'Please select a todo item to remove.')

    def pdf2txt(self, filename_list):
        # Open the PDF file
        for file in filename_list:
            print("pdf2txt ... 1", file)
            if(file[2] == "pdf"):
                pdf = fitz.open(file[1])  # Replace with your PDF file path
                # Iterate over each page in the PDF
                for page_num in range(len(pdf)):
                    print("pdf2txt ... 2")
                    page = pdf[page_num]  # Get the page
                    text = page.get_text()  # Extract text from the page
                    with open(f'{file[1][:-4]}.txt', 'a', encoding = 'utf-8') as myfile:
                        myfile.write(text)
                print("pdf2txt ... 3")
                # Close the PDF file
                pdf.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    todo_app = BatchConversion()
    todo_app.show()
    sys.exit(app.exec())