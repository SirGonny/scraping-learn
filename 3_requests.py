import requests

res = requests.get("http://google.com")
res.raise_for_status()

# if res.status_code == requests.codes.ok:
#   print("정상")
# else:
#   print("에러: ", res.status_code)

print(len(res.text))
print(res.text)

with open("mygoogle.html", "w", encoding="utf8") as f:
  f.write(res.text)