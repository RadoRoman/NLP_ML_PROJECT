import azapi
import selenium
from bs4 import BeautifulSoup
from selenium import webdriver

driver = webdriver.Chrome("../chromedriver_win32/chromedriver.exe")
driver.get('https://www.azlyrics.com/')

API = azapi.AZlyrics('google', accuracy=0.5)

API.artist = 'Ana Johnsson'
API.title = 'Bring It On'

API.getLyrics(save=True, ext='lrc')

print(API.lyrics)