from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.webdriver import Options

def run():
    driver = webdriver.Chrome()
    print('hi')
    # Open the webpage
    url = "http://localhost:8000/Homoglyphs.html"  # Replace with the URL of the target webpage
    driver.get(url)

    # Find all anchor tags <a>
    links = driver.find_elements(By.TAG_NAME, "a")
    if not links:
        print("No links!")
    ### INCLUDE CODE TO CHECK FOR HIDDEN
