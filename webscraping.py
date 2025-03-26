import requests
from bs4 import BeautifulSoup

url = "https://www.lenovo.com/in/en/c/laptops/thinkpad"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
print(soup.title.text)