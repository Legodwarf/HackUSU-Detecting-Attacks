def get_base_domain(url):
    # Remove the protocol (http, https, etc.) if present
    if "://" in url:
        url = url.split("://")[1]

    # Split by '/' to ignore any paths, and take the first part
    url = url.split("/")[0]

    return url

# Checks if a site has a different base url
def diff_site(url1, url2):
    return get_base_domain(url1) != get_base_domain(url2)
