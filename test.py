from bs4 import BeautifulSoup
import mechanize

session = mechanize.Browser()
req = session.open('https://cursos.alura.com.br/formacoes').read()

soup = BeautifulSoup(req, 'html.parser')
classes = ['formacoes__item', 'formacao__link']
links = []
a = soup.find('li', id="mobile", recursive=True)

for i in a.findChildren('a', class_=classes[1]):
    print(i['href'])
