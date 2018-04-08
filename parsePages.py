import urllib2
import string
from bs4 import BeautifulSoup

# Recieves a noticia bs4 page
def parseNoticia(noticiaSoup):
    article = noticiaSoup.find('article', id='nota')
    noticia = {}
    noticia['title'] = article.find('h1', class_ = 'titulo')
    cuerpo = article.find('section', id = 'cuerpo')
    paragraphs = [p.text.strip() for p in cuerpo.find_all('p')]
    noticia['cuerpo'] = string.join(paragraphs, ' ')
    print noticia
        
    

quote_page = 'https://www.lanacion.com.ar/'

# query the website and return the html to the variable 'page'
page = urllib2.urlopen(quote_page)

# parse the html using beautiful soup and store in variable 'soup'
soup = BeautifulSoup(page, 'html.parser')

# Take out the <div> of name and get its value
noticias = soup.find_all('article', class_= 'noticia')
for noticia in noticias:
    link = noticia.find('a')
    url = link['href'].strip()
    page = urllib2.urlopen(quote_page + url)
    noticiaSoup = BeautifulSoup(page, 'html.parser')
    parseNoticia(noticiaSoup)
    print url

