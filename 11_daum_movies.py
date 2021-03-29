import requests
from bs4 import BeautifulSoup as bs

for year in range(2015, 2022):
  if year == 2021:
    year = ""
  res = requests.get("https://search.daum.net/search?w=tot&q={}%EC%98%81%ED%99%94%EC%88%9C%EC%9C%84&DA=MOR&rtmaxcoll=MOR".format(year))
  res.raise_for_status()
  soup = bs(res.text, "lxml")

  images = soup.find_all("img", attrs={"class":"thumb_img"})

  for idx, image in enumerate(images):
    image_url = image["src"]
    if image_url.startswith("//"):
      image_url="https:"+image_url
    
    # print(image_url)
    image_res = requests.get(image_url)
    image_res.raise_for_status()

    if year == "":
      year = 2021
    with open("movie_{}_{}.jpg".format(year, idx+1), "wb") as f:
      f.write(image_res.content)
    
    if idx >= 4:
      break