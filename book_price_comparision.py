import requests
from bs4 import BeautifulSoup

id = input('Enter Id: ')


def flipkart():
    try:
        resp = requests.get('https://www.flipkart.com/indian-woman/p/itmdwuhbkmgugwjv?pid='+id).content
        jsoup = BeautifulSoup(resp, features="html.parser")
        domain = 'Flipkart'
        price1 = jsoup.find('div', attrs={'class': '_30jeq3 _16Jk6d'}).text
        book1 = jsoup.find('span', attrs={'class': 'B_NuCI'}).text.replace('\xa0\xa0', ' ')
        link1 = 'https://www.flipkart.com/indian-woman/p/itmdwuhbkmgugwjv?pid='+id
        dumy1 =  {'data':[domain, price1, book1, link1]}
        print(dumy1)
    except:
        error_msg = ['Not Available']
        print(error_msg)

# Bookswagon
def bookswagon():
    try:
        #id = data
        resp = requests.get('https://www.bookswagon.com/book/angel-answers-oracle-cards-radleigh/'+id).content
        jsoup = BeautifulSoup(resp, features="html.parser")
        domain = 'Bookswagon'
        price2 = jsoup.find('label', attrs={'id': 'ctl00_phBody_ProductDetail_lblourPrice'}).text
        book2 = jsoup.find('label', attrs={'id': 'ctl00_phBody_ProductDetail_lblTitle'}).text
        link2 = 'https://www.bookswagon.com/book/angel-answers-oracle-cards-radleigh/'+id
        dumy2 = {'data':[domain, price2, book2, link2]}
        print(dumy2)
    except:
        error_msg = ['Not Available']
        print(error_msg)

# spana
def spana():
    try:
        #id = data
        resp = requests.get('https://www.sapnaonline.com/books/'+id).content
        jsoup = BeautifulSoup(resp, features="html.parser")
        domain = 'SpanaOnline'
        price3 = jsoup.find('div', attrs={'class': 'sc-Axmtr AmountBlock__PriceText-zo5xbl-0 jleiXx'}).text
        book3 = jsoup.find('div', attrs={'class': 'sc-Axmtr ProductImageDetailCard__TitleText-xxaxm9-1 dJMXcH'}).text
        link3 = 'https://www.sapnaonline.com/books/'+id
        dumy3 = {'data':[domain, price3, book3, link3]}
        print(dumy3)
    except:
        error_msg = ['Not Available']
        print(error_msg)

# bookchor
def bookchor():
    try:
        #id = data
        resp = requests.get('https://www.bookchor.com/book/'+id).content
        jsoup = BeautifulSoup(resp, features="html.parser")
        domain = 'Bookchor'
        price4 = jsoup.find('span', attrs={'class': 'caption-subject bold uppercase pull-right'}).text.strip()
        book4 = jsoup.find('h1').text
        link4 = 'https://www.bookchor.com/book/'+id
        dumy4 =  {'data':[domain,price4, book4, link4]}
        print(dumy4)
    except:
        error_msg = ['Not Available']
        print(error_msg)


def all_():
   data =  [flipkart(),bookswagon(),spana(),bookchor()]
   return data
all_()