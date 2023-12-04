# task - 08

First of all when starting this task it was kind of difficult for me to get started as I didn't understand what was going on in main.py and search_window.py... It took me a while to reconstruct and understand the workflow of the program... 

Then the first thing that came to my mind was solving the problem with an object oriented approach. First I wanted to create a new class in the search_window.py file and have three different functions for each button (i.e: display button, capture button and search button). Whenever each button is pressed, using the instance of that class/object we could call the function associated with that particular button to produce the desired output... So whenever the search button is pressed, using an object ob of the new class the search function would be called... But it was quite challenging to link the search bar/place-holder to the function calling it... I had to use python lambda for linking the functions via the instance of the class which I found a little complex:

```python
enter_button.clicked.connect(lambda: self.bob.search_button(self.textbox))
```


So I scrapped all of that and decided to create three new python files for each button and imported all the files to the search_window.py file. For this it was much easier to use... I just passed the pokemon_name to each function in the python files to get the respective output using the following:

```python
from search import search_pokemon

class SearchWindow(QWidget):
    def __init__(self):
        super().__init__()
        
        #remaining code

        enter_button.clicked.connect(self.search_pokemon)

        def search_pokemon(self):
        pokemon_name = self.textbox.text()
        abilities, types, stats, art = search_pokemon(pokemon_name)

        #remaining code
```


This way it was easy to progress...
Some other difficulties that I faced during programming this were, adding the background image to the application's search_window, implementing previous and next buttons on the display_window that displays all the captured pokemon arts, downloading each pokemon artwork etc... 

Scraping the data from the api link was easier than I thought as finding each information was literally in a list of dictionaries...