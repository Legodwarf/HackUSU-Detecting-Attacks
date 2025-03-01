from pytrends.request import TrendReq
pytrends = TrendReq(hl='en-US', tz=360)

keywords = ['google.com','gооgle.com']

pytrends.build_payload(keywords, cat=0, timeframe='today 12-m', geo='', gprop='')
data = pytrends.interest_over_time()

print(data)