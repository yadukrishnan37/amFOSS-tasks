# task-05

Discord bot was one of the hardest tasks of the following main ones just cause of the fact that it took me a while to do the scraping part. 
Setting up the python virtual environment and creating a bot and storing the token of that bot in a .env file where all very simple after I watched some tips on Youtube... Coding the bot was also fairly simple. I downloaded most of the requirements using the following command after creating the requirements.txt

```bash
pip install -r requirements.txt
```
I finally started the scraping, which took a lot time... But then I used .contents library of BeautifulSoup4 which basically divided the html element based on the class to a list... Using that it was easier to search and scrape a particular tag of that html element and it's contents... Using loops it was possible to extract the respective data of each team like name, overs, summary and status of the match etc...