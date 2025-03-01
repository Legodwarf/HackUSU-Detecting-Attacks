from bs4 import BeautifulSoup
import requests


def has_hidden_href(url):
    """
    Checks if there's any <a> tag with an href that is hidden.
    Returns True if such a tag is found; otherwise, False.
    """
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    for tag in soup.find_all('a', href=True):  # Only consider <a> tags with an href
        style = tag.get('style', '')
        # Check for common hiding styles
        if 'display: none' in style or 'visibility: hidden' in style or 'opacity: 0' in style:
            return True

    return False

def check_hidden(val):
    if val:
        print("Flag 4 - Hidden Links")
