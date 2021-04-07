# import requests
# from bs4 import BeautifulSoup

# url = "https://play.google.com/store/movies/top"

# headers = {
#   "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36",
#   "Accept-Language":"ko-KR,ko"
# }

# res = requests.get(url, headers=headers)
# res.raise_for_status()
# soup = BeautifulSoup(res.text, "lxml")

# movies = soup.find_all("div", attrs={"class":"ImZGtf mpg5gc"})

# # print(len(movies))

# # with open("movie.html", "w", encoding="utf8") as f:
# #   f.write(soup.prettify())

# for movie in movies :
#   title = movie.find("div", attrs={"class":"WsMG1c nnK0zc"}).get_text()
#   print(title) 

from selenium import webdriver

browser = webdriver.Chrome()
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

