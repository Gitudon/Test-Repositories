import time
import requests
from bs4 import BeautifulSoup

url = "https://example.com"
time.sleep(1)
response = requests.get(url)
html = response.text

soup = BeautifulSoup(html, "html.parser")
h1_content = soup.find("h1").text if soup.find("h1") else None
print(h1_content)
