from selenium import webdriver
from selenium.webdriver.common.by import By
import unicodedata
import time
import http.server
import socketserver
import threading
# from pytrends.request import TrendReq
# pytrends = TrendReq(hl='en-US', tz=360)

def diff_site(url1, url2):
    return get_base_domain(url1) != get_base_domain(url2)

def normalize_domain(domain):
    # This is useful when you want to compare strings and eliminate subtle differences that may not be visually apparent (such as homoglyphs).
    rv = unicodedata.normalize("NFKC", domain) 
    print(" returned from the function: "+ rv)
    return rv

def get_base_domain(url):
    # Remove the protocol (http, https, etc.) if present
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
    
    normalized_site_name = normalize_domain(fake_url)
    # for_query_normalized = get_base_domain(normalized_site_name)
    # for_query_original = get_base_domain(fake_url)
    # print((for_query_normalized),(for_query_original))

    # correct upto here 
    # there is an issue here with how the data is being passed 

    
    from pytrends.request import TrendReq
    pytrends = TrendReq(hl='en-US', tz=360)
    #  keywords = [for_query_normalized,for_query_original]
    keywords = [normalized_site_name,fake_url]
    # keywords = ['google.com','gооgle.com']
    pytrends.build_payload(keywords, cat=0, timeframe='today 12-m', geo='', gprop='')
    data = pytrends.interest_over_time()
    print(data)


    #  before we get the data about the two sites, we want to know if we are already in // check if you are already on the site 
    
    # don't use get here we don't want to click on an infected site 
    # driver.get(f"{normalized_site_name}")
    #  fetch data about the site 


finally:
    # Close the browser
    driver.quit()
    # Stop the server
    httpd.shutdown()
    print("Server shut down.")
