# coding=utf-8
import urllib2
import string
import io
from bs4 import BeautifulSoup
import time

# Recieves a noticia bs4 page
def parseNoticia(noticiaSoup):
    article = noticiaSoup.find('article', id='nota')
    noticia = {}
    noticia['title'] = article.find('h1', class_ = 'titulo').get_text().strip()
    cuerpo = article.find('section', id = 'cuerpo')
    paragraphs = [p.get_text().strip() for p in cuerpo.find_all('p')]
    noticia['cuerpo'] = string.join(paragraphs, ' ')
    fileName = './news/' + noticia['title']+'.txt'
    with io.open(fileName, 'w') as file:
        file.write(noticia['cuerpo'])


quote_page = 'https://www.lanacion.com.ar/'

request_headers = {
"Accept-Language": "en-US,en;q=0.5",
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0",
"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
"Referer": "http://thewebsite.com",
"Connection": "keep-alive" 
}

request = urllib2.Request(quote_page, headers=request_headers)
# query the website and return the html to the variable 'page'
page = urllib2.urlopen(request).read()

# parse the html using beautiful soup and store in variable 'soup'
soup = BeautifulSoup(page, 'html.parser')

# Take out the <div> of name and get its value
noticias = soup.find_all('article', class_= 'noticia')
for noticia in noticias:
    try:
        link = noticia.find('a')
        url = link['href'].strip()
        print url
        request = urllib2.Request(quote_page + url, headers=request_headers)
        page = urllib2.urlopen(request).read()
        noticiaSoup = BeautifulSoup(page, 'html.parser')
        parseNoticia(noticiaSoup)
    except Exception: 
        pass
    
