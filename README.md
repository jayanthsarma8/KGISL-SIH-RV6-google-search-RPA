# KGISL-SIH-RV6-google-search-RPA
Project Title
                                    Google search Using Robotic process automation (RPA)
              
In recent framework, with huge development in the classic information retrieval system and use of the internet, searching and retrieving accurate information from the web still challenging task to research users. Our proposed system uses Robotic process automation (RPA) methods for searching information from Google and present the information in user requested format. Numerous RPA system was exist in the world which was used for different automation process.  The proposed system consist of three different components such as, Finding the user requested information, building the model using python standard URL Libraries function  and Regular Expression and presenting the information in user requested formats (Table format, CSV,Tex).


Prerequisites
Python 3.0 IDLE.   
Installing
Python Library Flies to be install       
Googel search 
pip install google (use Command promt to install)
url: https://pypi.org/project/google  
import re
import urllib.request,urllib.parse,urllib.error
from googlesearch import search
from bs4 import BeautifulSoup
import search1 as h
