import re

# abcd, book. desk
# ca?e
# care, cafe, case, cave
# a to z

p = re.compile("ca.e") 
# . : 하나의 문자를 의미
# ^ : 문자열의 시작
# $ : 문자열의 끝

def print_match(m):
  if m:
    print(m.group()) # 일치하는 문자열 반환
    print(m.string) # 입력받은 문자열
    print(m.start()) # 일치하는 문자열의 시작 index
    print(m.end()) # 일치하는 문자열의 끝 index
    print(m.span()) # 일치하는 문자열의 시작 / 끝 index
  else:
    print("매칭되지 않음")

# match : 주어진 문자열의 처음부터 일치하는지 확인
# m = p.match("careless")
# print_match(m)

# search : 주어진 문자열 중에 일치하는게 있는지 확인
# m = p.search("good care")
# print_match(m)

lst = p.findall("care cafe")
print(lst)  