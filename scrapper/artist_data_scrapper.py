
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome("../chromedriver_win32/chromedriver.exe")


for i in range(97, 98):
    driver.get('https://www.azlyrics.com/'+chr(i)+'.html')
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    html = soup.prettify("utf-8")
    artist = soup.find_all("div", {"class": "col-sm-6 text-center artist-col"})
    for name in artist:
        with open("myfile.txt", "a", encoding="utf-8") as f:
            f.write(name.text)

with open("myfile.txt", "r", encoding="utf-8") as f:
    for artist_name in f:
        f_letter_artist = artist_name[0].lower()
        artist_name_url = artist_name.lower().replace(' ','').replace('\n','')
        artist_url = rf"https://www.azlyrics.com/{f_letter_artist}/{artist_name_url}.html"

        driver.get(artist_url)
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        html = soup.prettify("utf-8")
        album = soup.find_all("div", {"class": "listalbum-item"})
        for name in album:
            with open("myfile2.txt", "a", encoding="utf-8") as f:
                f.write(name.text)