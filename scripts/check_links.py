import requests
from bs4 import BeautifulSoup

def check_all_links():
    homepage = requests.get("https://yourdomain.co.za").text
    soup = BeautifulSoup(homepage, "html.parser")
    
    for link in soup.find_all("a"):
        if requests.get(link["href"]).status_code != 200:
            AutoGPT(task=f"Update broken link: {link['href']}").execute()
