from selenium import webdriver
from selenium.webdriver.common.by import By
import unicodedata
import time
import http.server
import socketserver

# Function to normalize domain names
def normalize_domain(domain):
    # This is useful when you want to compare strings and eliminate subtle differences that may not be visually apparent (such as homoglyphs).
    rv = unicodedata.normalize("NFKC", domain) 
    print(" returned from the function: "+ rv)
    return rv

# Function to check for homoglyph attack
def is_homoglyph(fake_url, real_url):
    return normalize_domain(fake_url) != normalize_domain(real_url)

# only detects non latin 

PORT = 8000

Handler = http.server.SimpleHTTPRequestHandler
httpd = socketserver.TCPServer(("", PORT), Handler)
print(f"Serving at http://localhost:{PORT}")

# Run the server in the background
import threading
server_thread = threading.Thread(target=httpd.serve_forever, daemon=True)
server_thread.start()

# Set up Selenium WebDriver (Make sure you have chromedriver installed)
driver = webdriver.Chrome()

try:
    # Open the locally hosted page
    driver.get(f"http://localhost:{PORT}/Homoglyphs.html")

    # Wait for page to load
    time.sleep(2)

    # modification 
    fake_url_element = driver.find_element(By.CLASS_NAME, "fake-url")
    fake_url = fake_url_element.text.strip()

    # Define the real expected domain
    real_domain = "google.com"

    # Check for homoglyph attacpk

    if is_homoglyph(fake_url, real_domain):
        print(f"⚠️ Potential Homoglyph Attack Detected! Fake URL: {fake_url}")
    else:
        print(f"✅ No homoglyph attack detected.")

finally:
    # Close the browser
    driver.quit()
    # Stop the server
    httpd.shutdown()
    print("Server shut down.")
