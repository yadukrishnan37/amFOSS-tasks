import requests, os
from PySide6.QtWidgets import QLineEdit, QMessageBox, QLabel, QWidget, QPushButton, QApplication, QVBoxLayout
from PySide6.QtGui import QPixmap
from search import search_pokemon
from capture import capture_pokemon
from display import DisplayWindow

class SearchWindow(QWidget):
    def __init__(self):
        super().__init__()

        background_label = QLabel(self)
        background_pixmap = QPixmap("/home/yadukrishnan/Desktop/amFOSS23/Poke-Search/assets/landing.jpg")  
        background_label.setPixmap(background_pixmap)
        background_label.setGeometry(0, 0, background_pixmap.width(), background_pixmap.height())

        self.setFixedSize(850, 500)

        self.textbox = QLineEdit(self)
        self.textbox.setGeometry(50, 50, 280, 40)

        self.statlabel = QLabel(self)
        self.statlabel.setGeometry(470, 160, 500, 400)

        self.artlabel = QLabel(self)
        self.artlabel.setGeometry(470, 10, 280, 280)

        enter_button = QPushButton("Search", self)
        enter_button.setGeometry(50, 300, 160, 43)
        enter_button.clicked.connect(self.search_pokemon)

        capture_button = QPushButton("Capture", self)
        capture_button.setGeometry(50, 350, 160, 43)
        capture_button.clicked.connect(self.capture_pokemon)

        display_button = QPushButton("Display", self)
        display_button.setGeometry(50, 400, 160, 43)
        display_button.clicked.connect(self.show_display_window)

        self.display_window = DisplayWindow()  

    def search_pokemon(self):
        pokemon_name = self.textbox.text()
        abilities, types, stats, art = search_pokemon(pokemon_name)
        if abilities is not None:
            info_text = f"{pokemon_name.title()}\n\nAbilities: {abilities}\nTypes: {types}\n{stats}"
            self.statlabel.setText(info_text)
            self.display_artwork(art)

    def capture_pokemon(self):
        pokemon_name = self.textbox.text()
        result = capture_pokemon(pokemon_name)
        if result:
            QMessageBox.information(self, "Success", f"Artwork for {pokemon_name} captured successfully.")
            self.display_window.image_paths = self.display_window.get_captured_images() 
            self.display_window.show_image()    
        else:
            QMessageBox.critical(self, "Error", f"Failed to download artwork for {pokemon_name}.")

    def display_artwork(self, artwork_url):
        artwork_pixmap = QPixmap()
        artwork_data = requests.get(artwork_url).content
        artwork_pixmap.loadFromData(artwork_data)
        self.artlabel.setPixmap(artwork_pixmap)
        self.artlabel.setScaledContents(True)


    def show_display_window(self):
        self.display_window.show()

if __name__ == "__main__":
    import sys
    from PySide6.QtWidgets import QApplication

    app = QApplication(sys.argv)
    window = SearchWindow()
    window.show()
    sys.exit(app.exec())
