import time
from bs4 import BeautifulSoup
import requests
from requests import get
url = "https://taemovies.blogspot.com/2022/11/transformers-2007-bluray-1080p-720p-avc.html?m=1"

def flix(url):
    client = requests.session()
    r = client.get(url).text
    soup = BeautifulSoup (r, "html.parser")
    for a in soup.find_all("a"):
                   c = a.get("href")
                  
                   if "shortingly" in c:
                       
                       code = c.split("/")[-1]
                       DOMAIN = "https://go.techyjeeshan.xyz"
                       
                       final_url = f"{DOMAIN}/{code}"
                       resp = client.get(final_url)
                       soup = BeautifulSoup(resp.content, "html.parser")
    
                       try: inputs = soup.find(id="go-link").find_all(name="input")
                       except: return "Incorrect Link"
    
                       data = { input.get('name'): input.get('value') for input in inputs }

                       h = { "x-requested-with": "XMLHttpRequest" }
    
                       time.sleep(10)
                       r = client.post(f"{DOMAIN}/links/go", data=data, headers=h)
                       g = r.json()['url']
                       
                       t = client.get(g).text
                       soupt = BeautifulSoup(t, "html.parser")
                       title = soupt.title
                       gd_txt = f"{(title.text).replace('GDToT | ' , '')}\n{g}\n\n"
                       print(gd_txt)

print(flix(url))
