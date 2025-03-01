import http.server
import socketserver
import threading

from selenium import webdriver
from selenium.webdriver.common.by import By

import CheckSearchResults as CSR

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
    normalized_site_name = CSR.normalize_domain(fake_url)
    if not CSR.diff_site(fake_url, normalized_site_name):
        print("No flags triggered")
    else:
        print("Flag 1 -- ID'd search term is a different base url")
        CSR.Check_Search_Results(normalized_site_name, fake_url)

finally:
    driver.quit()
    httpd.shutdown()
    print("Server shut down.")
