
import requests
from bs4 import BeautifulSoup
from selenium import webdriver

options = webdriver.ChromeOptions()
options.headless = True
options.add_argument("window-size=1920x1080")

browser = webdriver.Chrome(options=options)
browser.maximize_window()

url = "https://play.google.com/store/movies/top"
browser.get(url)
# browser.execute_script("window.scrollTo(0, 1080)")
# browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")

import time

interval = 2
prev_height = browser.execute_script("return document.body.scrollHeight")

while True:
  browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")
  time.sleep(interval)
  current_height = browser.execute_script("return document.body.scrollHeight")
  if current_height == prev_height:
    break

  prev_height = current_height

print("완료")

browser.get_screenshot_as_file("google_movie.png")

soup = BeautifulSoup(browser.page_source, "lxml")

movies = soup.find_all("div", attrs={"class":"Vpfmgd"})

print(len(movies))

for movie in movies :
  title = movie.find("div", attrs={"class":"WsMG1c nnK0zc"}).get_text()

  original_price = movie.find("span", attrs={"class":"SUZt4c djCuy"})
  if original_price:
    original_price = original_price.get_text()
  else:
    continue

  price = movie.find("span", attrs={"class":"VfPpfd ZdBevf i5DZme"}).get_text()

  link = movie.find("a", attrs={"class":"JC71ub"})["href"]

  # print(f"제목:{title}")
  # print(f"할인전:{original_price}")
  # print(f"제목:{price}")
  # print("링크 : https://play.google.com"+link)
  # print("--------------------------")

  browser.quit()
