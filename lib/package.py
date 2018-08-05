import urllib.request
#import ssl
#import re
#import os
import urllib.request as req
from bs4 import BeautifulSoup
from subprocess import call # module to create subprogram inside our program

choice=input("Please Enter The Download Path :\n").replace("\ ","/")
os.chdir(choice)
