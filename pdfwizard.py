from uifile import Ui_MainWindow
from PySide6.QtWidgets import *
import sys
import os
import win32com.client
import win32api



class PdfWizard(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Pdf Wizard")

        self.create_button.clicked.connect(self.switch_createpage)
        self.mainconvert_button.clicked.connect(self.switch_convertpage)
        self.extract_button.clicked.connect(self.switch_extractpagepage)
        self.split_button.clicked.connect(self.switch_splitpage)
        self.insert_button.clicked.connect(self.switch_insertpage)
        self.merge_button.clicked.connect(self.switch_mergepage)
        self.protect_button.clicked.connect(self.switch_protectpage)
        self.watermark_button.clicked.connect(self.switch_watermarkpage)

        self.selectFile_button.clicked.connect(self.select_file)
        self.convert_button.clicked.connect(self.doc_to_pdf)

        self.selected_file_path = ""

    def select_file(self):
        options = QFileDialog.Options()
        file_path, _ = QFileDialog.getOpenFileName(self, "Select File", "", "All Files (*)", options=options)
        if file_path:
            self.selected_file_path = file_path
            self.selectFile_line.setText(file_path)

    def doc_to_pdf(self):
        wdFormatPDF = 17

        word = win32com.client.Dispatch('Word.Application')

        file_path = self.selected_file_path
        filename = os.path.split(file_path)[1]
        print("File path:", file_path)  # Print file path for debugging
        try:
            # Convert the file path to the short path format
            short_path = win32api.GetShortPathName(file_path)
            print("Short path:", short_path)  # Print short path for debugging

            doc = word.Documents.Open(short_path)
            pdf_file_path = os.path.splitext(short_path)[0] + ".pdf"
            print("PDF file path:", pdf_file_path)  # Print PDF file path for debugging
            doc.SaveAs(pdf_file_path, FileFormat=wdFormatPDF)
            doc.Close()
            word.Quit()
        except Exception as e:
            print("Error:", str(e))  # Print any exceptions for debugging


    def switch_createpage(self):
        self.stackedWidget.setCurrentWidget(self.create_page)

    def switch_convertpage(self):
        self.stackedWidget.setCurrentWidget(self.convert_page)
    
    def switch_extractpagepage(self):
        self.stackedWidget.setCurrentWidget(self.extract_page)

    def switch_splitpage(self):
        self.stackedWidget.setCurrentWidget(self.split_page)
    def switch_insertpage(self):
        self.stackedWidget.setCurrentWidget(self.insert_page)
    
    def switch_mergepage(self):
        self.stackedWidget.setCurrentWidget(self.merge_page)

    def switch_protectpage(self):
        self.stackedWidget.setCurrentWidget(self.protect_page)

    def switch_watermarkpage(self):
        self.stackedWidget.setCurrentWidget(self.watermark_page)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PdfWizard()
    window.show()
    sys.exit(app.exec())

