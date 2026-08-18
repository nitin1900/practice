import requests,BeautifulSoup
url='http://www.vanityfair.com/society/2014/06/monica-lewinsky-humiliation-culture'
soup=BeautifulSoup(requests.get(url).text)

body = soup.select("div.parbase.cn_text > div.body > p")

for elem in body[7:]:
  print(elem.text)
