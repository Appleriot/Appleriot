import requests
from bs4 import BeautifulSoup

tags = input("Enter tags:")
links = input("Enter your website link:")

url = links
reqs = requests.get(url)
soup = BeautifulSoup(reqs.text, 'html.parser')

urls = []
for link in soup.find_all(tags):
    print(link.get('href')[:25])

