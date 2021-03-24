import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/weekday.nhn"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")

# print(soup.a)
# print(soup.a.attrs)
# print(soup.a["href"])

# print(soup.find("a", attrs={"class":"Nbtn_upload"}))
# print(soup.find("li", attrs={"class":"rank01"}))
# rank1 = soup.find("li", attrs={"class":"rank01"})
# print(rank1.a.get_text())
# print(rank1.next_sibling)
# print(rank1.previous_sibling)
# print(rank1.next_sibling.next_sibling)

# print(rank1.parent)
# rank1.find_next_siblings("li")

webtoon = soup.find("a", text="")