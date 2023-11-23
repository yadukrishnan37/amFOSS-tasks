import os
from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout, QPushButton, QHBoxLayout
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt


class DisplayWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Captured Pokemon Images")
        self.setGeometry(100, 100, 600, 400)

        self.image_paths = self.get_captured_images()
        self.current_index = 0

        self.image_label = QLabel(self)
        self.image_label.setAlignment(Qt.AlignCenter)

        self.prev_button = QPushButton("Previous", self)
        self.prev_button.clicked.connect(self.prev)

        self.next_button = QPushButton("Next", self)
        self.next_button.clicked.connect(self.next)

        layout = QVBoxLayout(self)
        layout.addWidget(self.image_label)
        
        button_layout = QHBoxLayout()
        button_layout.addWidget(self.prev_button)
        button_layout.addWidget(self.next_button)
        layout.addLayout(button_layout)

    def prev(self):
        if self.image_paths:
            self.current_index = (self.current_index - 1) % len(self.image_paths)
            self.show_image()

    def next(self):
        if self.image_paths:
            self.current_index = (self.current_index + 1) % len(self.image_paths)
            self.show_image()

    def get_captured_images(self):
        parent_path = "/home/yadukrishnan/Desktop/amFOSS23/Poke-Search/assets/captures/"
        filenames = os.listdir(parent_path)
        file_paths = [os.path.join(parent_path, filename) for filename in filenames]
        return file_paths

    def show_image(self):
        if self.image_paths:
            image_path = self.image_paths[self.current_index]
            pixmap = QPixmap(image_path)
            self.image_label.setPixmap(pixmap)
            self.image_label.setScaledContents(True)
