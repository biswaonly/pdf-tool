from PySide6.QtWidgets import *
from pdfwizard import PdfWizard
import sys

app = QApplication(sys.argv)

window = PdfWizard()

window.show()
app.exec()