from setuptools import setup

APP = ['main.py']  # The main entry point of your application
DATA_FILES = ['pdf_icon.icns', 'bg.jpeg']  # Include your icon and other resources
OPTIONS = {
    'argv_emulation': True,
    'packages': ['PySide6', 'fitz', 'win32com', 'win32api'],  # List your dependencies here
    'iconfile': 'app_icon.icns',  # Your application icon in .icns format
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
