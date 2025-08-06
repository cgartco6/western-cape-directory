import requests
from bs4 import BeautifulSoup
import smtplib  # Using Afrihost's 25 free emails

def check_links():
    base_url = "https://yourdomain.co.za"
    response = requests.get(base_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    broken = []
    for link in soup.find_all('a'):
        url = link.get('href')
        if not url.startswith('http'):
            url = base_url + url
        
        if requests.get(url).status_code != 200:
            broken.append(url)
    
    if broken:
        send_alert(broken)

def send_alert(links):
    with smtplib.SMTP('mail.afrihost.co.za', 587) as server:
        server.login('admin@yourdomain.co.za', 'email_password')
        message = f"Subject: Broken Links Found\n\n{', '.join(links)}"
        server.sendmail('admin@yourdomain.co.za', 'owner@email.com', message)
