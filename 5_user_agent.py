import requests

url = "http://google.com"
headers = {"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36"}
res = requests.get(url, headers=headers)
res.raise_for_status()

with open("mygoogle.html", "w", encoding="utf8") as f:
  f.write(res.text)