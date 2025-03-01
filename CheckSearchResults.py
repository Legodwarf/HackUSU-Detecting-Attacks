from pytrends.request import TrendReq
import unicodedata
def normalize_domain(domain):
    normalized = domain.replace("о", "o")
    print(normalized)
    return normalized

def diff_site(url1, url2):
    print(url1)
    print(url2)
    return get_base_domain(url1) != get_base_domain(url2)

def get_base_domain(url):
    if "://" in url:
        url = url.split("://")[1]

    if "/" in url:
        url = url.split("/")[0]
    return url

def Check_Search_Results(normalized_site_name, fake_url):
    for_query_normalized = get_base_domain(normalized_site_name)
    for_query_original = get_base_domain(fake_url)

    pytrends = TrendReq(hl='en-US', tz=360)
    keywords = [for_query_original, for_query_normalized]
    pytrends.build_payload(keywords, cat=0, timeframe='today 12-m', geo='', gprop='')
    data = pytrends.interest_over_time()
    if .2 * data.iloc[1, 0] < data.iloc[1, 1]:
        print("Flag 2 -- ID'd search term is much less popular than latin equivalent")