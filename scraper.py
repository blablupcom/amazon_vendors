from datetime import datetime
from bs4 import BeautifulSoup as bs
import requests
import scraperwiki
import itertools
import json


def scrape_asins(base_url, vendors):
    for vendor in vendors:
        asin_num = []
        for page in itertools.count():
            data = {'seller':'{}'.format(vendor), 'currentPage': '{}'.format(page + 1), 'useMYI': '0'}
            print data
            pages = requests.post(base_url, data=data)
            soup = json.loads(pages.text)
            if soup:
                asin_num.extend(soup)
            else:
                break
        for i, asin in enumerate(asin_num):
            prices = requests.get('http://www.amazon.com/gp/aag/ajax/asinRenderToJson.html?id={0}&useMYI=0&numCellsInResultsSet=2400&isExplicitSearch=0&merchantID={1}&shovelerName=AAGProductWidget&maxCellsPerPage=1'.format(asin, vendor))
            li = json.loads(prices.text)
            sp = bs(li[0]['content'])
            price = sp.find('li', 'AAG_ProductPrice aagItemDetLI').text
            todays_date = str(datetime.now())
            scraperwiki.sqlite.save(unique_keys=['Date'], data={"Seller ID": vendor, "ASIN": asin.strip(), "Price": price.strip(), "Date": todays_date})
            print i, price, asin


def scrape(vendors):
    base_url = 'http://www.amazon.com/gp/aag/ajax/searchResultsJson.html'
    scrape_asins(base_url, vendors)


if __name__ == '__main__':
    vendors = ['A1RA39XAINC4DN']
    scrape(vendors)