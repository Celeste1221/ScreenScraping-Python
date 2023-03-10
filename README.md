# ScreenScraping-Python
A python application that allows the user to enter the url of a website they would like to scrape for content and the specific content they are looking for. 
The program will return all the instances of that content found in the web page hierarchy. It uses the wx library to create a graphical interface that gets user input and displays output. It uses the beautifulsoup4 library for scraping and extraction, it uses the python urllib library for url parsing and other url handling tasks.

## Dependencies
```
$ pip install beautifulsoup4  
$ pip install urllib  
$ pip install -U wxPython
```
```
import wx  
from bs4 import BeautifulSoup  
import urllib.request
```

## Useful websites
On Beautiful Soup: https://www.crummy.com/software/BeautifulSoup/bs4/doc/](https://beautiful-soup-4.readthedocs.io/en/latest/)  
On wxWidgets: https://docs.wxpython.org/
