from bs4 import BeautifulSoup
import mechanize, os
from http.cookiejar import CookieJar

liga = 'https://cursos.alura.com.br'

class AluraLogin(object):
        def __init__(self, user, password):
            cj = CookieJar()
            self._session = mechanize.Browser()
            self._session.set_handle_robots(False)
            self._session.set_cookiejar(cj)
            self._session.open("https://cursos.alura.com.br/loginForm")
            self._session.select_form(nr=1)
            self._session.form['username'] = user
            self._session.form['password'] = password


class AluraCrawler():
        def __init__(self, session):
            self._session = session
            self._session.submit()
            self._principal = self._session.open('https://cursos.alura.com.br/formacoes').read()

        def choose_formation(self):
            categorias = self.__categories_crawler()
            categoria = self.__listing(categorias)
            formacoes = self.__formations_crawler()
            formacao = self.__listing(formacoes)
            print(formacao + 'choosen...')
            return ['https://cursos.alura.com.br' + formacao]

        def __categories_crawler(self):
            lista_categoria = ['formacoes__item']
            links = self._text_scraper(lista_categoria, self._principal, prop='id')
            return links

        def __formations_crawler(self):
            lista_formacao = ['formacao__link']
            links = self._text_scraper(lista_formacao, self._principal, tag='a', prop='href')
            return links

        def formation_crawler(self, lst, aux=0):
            classes = ['learning-content__link', 'courseSectionList-section', 'task-menu-nav-item-link-VIDEO']
            for link in lst:
                req = self._session.open(link).read()
                links = self.__link_crawler(classes, req, aux)
                print(links)

            if aux < 2:
                print(str(aux*20) + '%')
                return self.formation_crawler(lst=links, aux=aux+1)
            return links

        def __link_crawler(self, classes, req, aux=0):
            links = []
            soup = BeautifulSoup(req, 'html.parser')
            for a in soup.find_all('a', class_=classes[aux]):
                if a['href'].startswith('/'):
                    print(a['href'])
                    links.append(liga + a['href'])
            return links

        def __listing(self, opcoes):
            clear = lambda: os.system('cls')
            while (True):
                escolha = ''
                clear()
                print(' | '.join(str(i) for i in opcoes))
                print('Selecione uma das opções:')
                opcao = input()
                for i in opcoes:
                    if opcao in i and opcoes:
                        escolha = i
                        break
                if escolha:
                    break
            return escolha

        def _text_scraper(self, classe, req, tag='li', prop=None):
            links = []
            soup = BeautifulSoup(req, 'html.parser')
            for a in soup.find_all(tag, class_=classe):
                links.append(a[prop])
            return links

class AluraScraper():
    def __init__(self, session):
        self._session = session

    def scraper(self, links):
        result = []
        for link in links:
            print(link + '/video')
            req = self._session.open(link + '/video').read()
            result.append(req)
        try:
            os.remove('data.txt')
        except OSError:
            pass
        with open('data.txt', 'w') as f:
            for item in result:
                f.write(f'{item}\n')
        print('Done! Saved in data.txt')
