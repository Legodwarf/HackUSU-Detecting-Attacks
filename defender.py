from selenium import webdriver
from selenium.webdriver.common.by import By
import unicodedata
import time
import http.server
import socketserver
import threading
from pytrends.request import TrendReq
import pandas as pd

def diff_site(url1, url2):
    return get_base_domain(url1) != get_base_domain(url2)

def normalize_domain(domain):
    # This is useful when you want to compare strings and eliminate subtle differences that may not be visually apparent (such as homoglyphs).
    normalized = unicodedata.normalize('NFKC',domain)
    normalized = normalized.replace("о", "o")
    print(normalized)
    return normalized


def get_base_domain(url):
    if "://" in url:
        url = url.split("://")[1]        

    if "/" in url:
        url = url.split("/")[0]
    return url    

PORT = 8000

Handler = http.server.SimpleHTTPRequestHandler
httpd = socketserver.TCPServer(("", PORT), Handler)
print(f"Serving at http://localhost:{PORT}")

server_thread = threading.Thread(target=httpd.serve_forever, daemon=True)
server_thread.start()

driver = webdriver.Chrome()

try:
    driver.get(f"http://localhost:{PORT}/Homoglyphs.html")

    # accessing the fake url thru the element this will have to modfied 
    fake_url_element = driver.find_element(By.CLASS_NAME, "fake-url")
    fake_url = fake_url_element.text.strip()

    # Check 1
    normalized_site_name = normalize_domain(fake_url)
    if diff_site("fake_url", normalized_site_name):
        print("Flag 1 -- ID'd search term is a different base url")
    

    #print(normalized_site_name)
    for_query_normalized = get_base_domain(normalized_site_name)
    for_query_original = get_base_domain(fake_url)

    print((for_query_normalized),(for_query_original))

    # correct upto here 
    # there is an issue here with how the data is being passed 

    pytrends = TrendReq(hl='en-US', tz=360)
    keywords = [for_query_original, for_query_normalized]
    pytrends.build_payload(keywords, cat=0, timeframe='today 12-m', geo='', gprop='')
    data = pytrends.interest_over_time()
    if .2 * data.iloc[1,0] < data.iloc[1,1]:
        print("Flag 2 -- ID'd search term is much less popular than latin equivalent")


    #  before we get the data about the two sites, we want to know if we are already in // check if you are already on the site 
    
    # don't use get here we don't want to click on an infected site 
    # driver.get(f"{normalized_site_name}")
    #  fetch data about the site 


finally:
    driver.quit()
    httpd.shutdown()
    print("Server shut down.")
